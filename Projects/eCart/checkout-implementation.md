# E-commerce Checkout and Order Processing Implementation Guide

## Table of Contents
1. [Overview](#overview)
2. [Implementation Steps](#implementation-steps)
3. [Required Components](#required-components)
   - [Frontend Components](#frontend-components)
   - [Backend Updates](#backend-updates)
4. [Component Code](#component-code)
   - [CheckoutPage.jsx](#checkoutpagejsx)
   - [Updated PaymentForm.jsx](#updated-paymentformjsx)
   - [OrderConfirmationPage.jsx](#orderconfirmationpagejsx)
   - [OrdersPage.jsx](#orderspagejsx)
   - [CartPage.jsx](#cartpagejsx)
   - [Updated CartContext.jsx](#updated-cartcontextjsx)
   - [Updated App.jsx](#updated-appjsx)
5. [Backend Enhancements](#backend-enhancements)
   - [Updated OrderService.js](#updated-orderservicejs)
   - [Shipping Info Database Schema](#shipping-info-database-schema)
6. [Testing the Order Flow](#testing-the-order-flow)

## Overview

This guide outlines the implementation of a complete checkout and order processing system for your e-commerce application, building on your existing order model, service, and controller structure.

**The Complete Order Flow:**

1. User reviews items in cart
2. User clicks "Checkout" button
3. User enters shipping information
4. User enters payment information
5. Order is created in database with "pending" status
6. Payment is processed via Stripe
7. Order status is updated to "paid"
8. User is redirected to order confirmation page
9. Order history is available in user account

## Implementation Steps

1. Create a checkout page with shipping form and payment integration
2. Update the payment form to work with cart data
3. Create an order confirmation page
4. Enhance the orders page to show order history
5. Update CartContext to handle checkout navigation
6. Update App.jsx with new routes
7. Enhance OrderService to handle shipping information
8. Create a shipping info table in the database

## Required Components

### Frontend Components

- **CheckoutPage**: Displays cart summary and collects shipping/payment information
- **PaymentForm** (updated): Processes payments through Stripe
- **OrderConfirmationPage**: Shows details after successful order
- **OrdersPage** (enhanced): Displays user's order history
- **CartPage** (with checkout button): Allows navigation to checkout

### Backend Updates

- **OrderService** (enhanced): Support for shipping information
- **Database Schema**: New shipping_info table

## Component Code

### CheckoutPage.jsx

```jsx
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';
import PaymentForm from '../components/PaymentForm';

const CheckoutPage = () => {
    const { user } = useAuth();
    const { cartItems, cartTotal, clearCart } = useCart();
    const navigate = useNavigate();
    
    const [shippingInfo, setShippingInfo] = useState({
        name: '',
        address: '',
        city: '',
        state: '',
        zip: '',
        email: ''
    });
    
    const [orderCreated, setOrderCreated] = useState(false);
    const [orderId, setOrderId] = useState(null);
    
    // Redirect to login if not authenticated
    useEffect(() => {
        if (!user) {
            navigate('/login', { state: { from: '/checkout' } });
        }
    }, [user, navigate]);
    
    // Handle shipping info changes
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setShippingInfo(prev => ({
            ...prev,
            [name]: value
        }));
    };
    
    // Format cart items for order creation
    const getOrderItems = () => {
        return cartItems.map(item => ({
            productId: item.product_id,
            quantity: item.quantity,
            unitPrice: item.price
        }));
    };
    
    // Handle successful payment
    const handlePaymentSuccess = (orderId) => {
        setOrderCreated(true);
        setOrderId(orderId);
        clearCart();
        
        // Redirect to order confirmation
        setTimeout(() => {
            navigate(`/order-confirmation/${orderId}`);
        }, 1500);
    };
    
    if (!user || cartItems.length === 0) {
        return <div className="container mx-auto p-4">Loading...</div>;
    }
    
    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-6">Checkout</h1>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {/* Left Column - Cart Summary */}
                <div>
                    <h2 className="text-xl font-semibold mb-4">Order Summary</h2>
                    <div className="bg-gray-50 p-4 rounded-lg">
                        {cartItems.map(item => (
                            <div key={item.product_id} className="flex justify-between py-2 border-b">
                                <div>
                                    <p className="font-medium">{item.title}</p>
                                    <p className="text-sm text-gray-600">Qty: {item.quantity}</p>
                                </div>
                                <p className="font-medium">${(item.price * item.quantity).toFixed(2)}</p>
                            </div>
                        ))}
                        
                        <div className="mt-4 pt-2 border-t">
                            <div className="flex justify-between font-semibold">
                                <span>Total:</span>
                                <span>${cartTotal.toFixed(2)}</span>
                            </div>
                        </div>
                    </div>
                    
                    {/* Shipping Info Form */}
                    <div className="mt-6">
                        <h2 className="text-xl font-semibold mb-4">Shipping Information</h2>
                        <div className="space-y-3">
                            <div>
                                <label className="block text-sm font-medium mb-1">Full Name</label>
                                <input
                                    type="text"
                                    name="name"
                                    value={shippingInfo.name}
                                    onChange={handleInputChange}
                                    className="w-full p-2 border rounded"
                                    required
                                />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Address</label>
                                <input
                                    type="text"
                                    name="address"
                                    value={shippingInfo.address}
                                    onChange={handleInputChange}
                                    className="w-full p-2 border rounded"
                                    required
                                />
                            </div>
                            <div className="grid grid-cols-2 gap-3">
                                <div>
                                    <label className="block text-sm font-medium mb-1">City</label>
                                    <input
                                        type="text"
                                        name="city"
                                        value={shippingInfo.city}
                                        onChange={handleInputChange}
                                        className="w-full p-2 border rounded"
                                        required
                                    />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium mb-1">State</label>
                                    <input
                                        type="text"
                                        name="state"
                                        value={shippingInfo.state}
                                        onChange={handleInputChange}
                                        className="w-full p-2 border rounded"
                                        required
                                    />
                                </div>
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">ZIP Code</label>
                                <input
                                    type="text"
                                    name="zip"
                                    value={shippingInfo.zip}
                                    onChange={handleInputChange}
                                    className="w-full p-2 border rounded"
                                    required
                                />
                            </div>
                            <div>
                                <label className="block text-sm font-medium mb-1">Email</label>
                                <input
                                    type="email"
                                    name="email"
                                    value={shippingInfo.email}
                                    onChange={handleInputChange}
                                    className="w-full p-2 border rounded"
                                    required
                                />
                            </div>
                        </div>
                    </div>
                </div>
                
                {/* Right Column - Payment */}
                <div>
                    <h2 className="text-xl font-semibold mb-4">Payment</h2>
                    <div className="bg-gray-50 p-4 rounded-lg">
                        <PaymentForm 
                            userId={user.uid}
                            orderItems={getOrderItems()}
                            shippingInfo={shippingInfo}
                            onPaymentSuccess={handlePaymentSuccess}
                        />
                    </div>
                </div>
            </div>
            
            {orderCreated && (
                <div className="mt-6 p-4 bg-green-100 text-green-800 rounded-lg">
                    Order created successfully! Redirecting to order confirmation...
                </div>
            )}
        </div>
    );
};

export default CheckoutPage;
```

### Updated PaymentForm.jsx

```jsx
import React, { useState } from "react";
import { useStripe, useElements, CardElement } from "@stripe/react-stripe-js";
import { API_BASE_URL } from "../config/constants";

const PaymentForm = ({ userId, orderItems, shippingInfo, onPaymentSuccess }) => {
    const stripe = useStripe();
    const elements = useElements();
    const [loading, setLoading] = useState(false);
    const [errorMessage, setErrorMessage] = useState("");

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!stripe || !elements) return;
        if (!userId || !orderItems || orderItems.length === 0) {
            setErrorMessage("Invalid order data");
            return;
        }
    
        setLoading(true);
        setErrorMessage("");
    
        try {
            // Step 1: Create an order and get clientSecret
            const response = await fetch(`${API_BASE_URL}/api/orders`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    userId,
                    orderItems,
                    shippingInfo
                }),
            });
    
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || "Failed to create order");
            }
    
            const { order, clientSecret } = await response.json();
    
            // Step 2: Confirm payment with Stripe
            const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
                payment_method: { card: elements.getElement(CardElement) },
            });
    
            if (error) {
                throw new Error(error.message);
            }
    
            // Step 3: Send stripePaymentId to backend to update order status
            const updateResponse = await fetch(`${API_BASE_URL}/api/orders/${order.id}/update-payment`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ stripePaymentId: paymentIntent.id }),
            });
            
            if (!updateResponse.ok) {
                throw new Error("Payment confirmed but failed to update order");
            }
    
            // Notify parent component of success
            onPaymentSuccess(order.id);
        } catch (error) {
            setErrorMessage(error.message || "Payment processing error");
        } finally {
            setLoading(false);
        }
    };
    
    return (
        <form onSubmit={handleSubmit} className="mt-5">
            <div className="mb-6">
                <label className="block text-sm font-medium mb-2">
                    Card Details
                </label>
                <div className="p-3 border rounded-md bg-white">
                    <CardElement
                        options={{
                            style: {
                                base: {
                                    fontSize: "16px",
                                    color: "#424770",
                                    "::placeholder": {
                                        color: "#aab7c4",
                                    },
                                },
                                invalid: {
                                    color: "#9e2146",
                                },
                            },
                        }}
                    />
                </div>
            </div>
            
            {errorMessage && (
                <div className="text-red-500 mb-4">{errorMessage}</div>
            )}
            
            <button
                type="submit"
                disabled={!stripe || loading}
                className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 disabled:bg-gray-400"
            >
                {loading ? "Processing..." : "Complete Order"}
            </button>
        </form>
    );
};

export default PaymentForm;
```

### OrderConfirmationPage.jsx

```jsx
import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { API_BASE_URL } from '../config/constants';

const OrderConfirmationPage = () => {
    const { orderId } = useParams();
    const [order, setOrder] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchOrderDetails = async () => {
            try {
                const response = await fetch(`${API_BASE_URL}/api/orders/${orderId}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch order details');
                }
                
                const data = await response.json();
                setOrder(data);
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };
        
        fetchOrderDetails();
    }, [orderId]);
    
    if (loading) {
        return <div className="container mx-auto p-4">Loading order details...</div>;
    }
    
    if (error) {
        return (
            <div className="container mx-auto p-4">
                <div className="bg-red-100 text-red-800 p-4 rounded-lg">
                    {error}
                </div>
                <Link to="/orders" className="mt-4 text-blue-500 hover:underline block">
                    View All Orders
                </Link>
            </div>
        );
    }
    
    return (
        <div className="container mx-auto p-4">
            <div className="bg-green-100 text-green-800 p-4 rounded-lg mb-6">
                <h1 className="text-xl font-bold">Order Confirmed!</h1>
                <p>Your order has been successfully placed.</p>
            </div>
            
            <div className="bg-white shadow-md rounded-lg p-6 mb-6">
                <h2 className="text-xl font-semibold mb-4">Order Summary</h2>
                <div className="mb-4">
                    <p><span className="font-medium">Order ID:</span> {orderId}</p>
                    <p><span className="font-medium">Date:</span> {new Date(order[0].created_at).toLocaleDateString()}</p>
                    <p><span className="font-medium">Status:</span> {order[0].status}</p>
                </div>
                
                <h3 className="text-lg font-medium mb-2">Items</h3>
                <div className="divide-y">
                    {order.map((item, index) => (
                        <div key={index} className="py-3 flex justify-between">
                            <div>
                                <p className="font-medium">{item.product_title}</p>
                                <p className="text-sm text-gray-600">Quantity: {item.quantity}</p>
                            </div>
                            <p className="font-medium">${parseFloat(item.unit_price).toFixed(2)}</p>
                        </div>
                    ))}
                </div>
                
                <div className="mt-4 pt-3 border-t">
                    <div className="flex justify-between font-semibold">
                        <span>Total:</span>
                        <span>${parseFloat(order[0].total_price).toFixed(2)}</span>
                    </div>
                </div>
            </div>
            
            <div className="flex justify-between">
                <Link to="/" className="text-blue-500 hover:underline">
                    Continue Shopping
                </Link>
                <Link to="/orders" className="text-blue-500 hover:underline">
                    View All Orders
                </Link>
            </div>
        </div>
    );
};

export default OrderConfirmationPage;
```

### OrdersPage.jsx

```jsx
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { API_BASE_URL } from '../config/constants';

const OrdersPage = () => {
    const { user } = useAuth();
    const [orders, setOrders] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchOrders = async () => {
            if (!user) return;
            
            try {
                const response = await fetch(`${API_BASE_URL}/api/orders/user/${user.uid}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch orders');
                }
                
                const data = await response.json();
                
                // Group by order_id
                const groupedOrders = data.reduce((acc, item) => {
                    if (!acc[item.order_id]) {
                        acc[item.order_id] = {
                            id: item.order_id,
                            date: new Date(item.created_at),
                            status: item.status,
                            totalPrice: parseFloat(item.total_price),
                            items: []
                        };
                    }
                    
                    acc[item.order_id].items.push({
                        product_title: item.product_title,
                        quantity: item.quantity,
                        unitPrice: parseFloat(item.unit_price)
                    });
                    
                    return acc;
                }, {});
                
                setOrders(Object.values(groupedOrders));
                setLoading(false);
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };
        
        fetchOrders();
    }, [user]);
    
    if (!user) {
        return (
            <div className="container mx-auto p-4">
                <p>Please log in to view your orders.</p>
                <Link to="/login" className="text-blue-500 hover:underline">
                    Log In
                </Link>
            </div>
        );
    }
    
    if (loading) {
        return <div className="container mx-auto p-4">Loading orders...</div>;
    }
    
    if (error) {
        return (
            <div className="container mx-auto p-4">
                <div className="bg-red-100 text-red-800 p-4 rounded-lg">
                    {error}
                </div>
            </div>
        );
    }
    
    if (orders.length === 0) {
        return (
            <div className="container mx-auto p-4">
                <h1 className="text-2xl font-bold mb-6">My Orders</h1>
                <div className="bg-gray-100 p-6 rounded-lg text-center">
                    <p className="mb-4">You don't have any orders yet.</p>
                    <Link to="/" className="text-blue-500 hover:underline">
                        Start Shopping
                    </Link>
                </div>
            </div>
        );
    }
    
    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-6">My Orders</h1>
            
            <div className="space-y-6">
                {orders.map(order => (
                    <div key={order.id} className="bg-white shadow-md rounded-lg p-6">
                        <div className="flex justify-between mb-4">
                            <div>
                                <p className="text-sm text-gray-500">Order placed</p>
                                <p className="font-medium">{order.date.toLocaleDateString()}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-500">Order #</p>
                                <p className="font-medium">{order.id}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-500">Total</p>
                                <p className="font-medium">${order.totalPrice.toFixed(2)}</p>
                            </div>
                            <div>
                                <p className="text-sm text-gray-500">Status</p>
                                <p className={`font-medium ${
                                    order.status === 'delivered' ? 'text-green-600' : 
                                    order.status === 'shipped' ? 'text-blue-600' : 
                                    order.status === 'paid' ? 'text-purple-600' :
                                    'text-gray-600'
                                }`}>
                                    {order.status.charAt(0).toUpperCase() + order.status.slice(1)}
                                </p>
                            </div>
                        </div>
                        
                        <div className="divide-y">
                            {order.items.map((item, index) => (
                                <div key={index} className="py-3 flex justify-between">
                                    <div>
                                        <p className="font-medium">{item.product_title}</p>
                                        <p className="text-sm text-gray-600">Quantity: {item.quantity}</p>
                                    </div>
                                    <p className="font-medium">${item.unitPrice.toFixed(2)}</p>
                                </div>
                            ))}
                        </div>
                        
                        <Link 
                            to={`/order-confirmation/${order.id}`} 
                            className="mt-4 text-blue-500 hover:underline block text-right"
                        >
                            View Order Details
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default OrdersPage;
```

### CartPage.jsx

```jsx
import React from 'react';
import { useCart } from '../context/CartContext';
import { Link } from 'react-router-dom';

const CartPage = () => {
    const { 
        cartItems, 
        cartTotal, 
        removeFromCart, 
        updateQuantity, 
        proceedToCheckout 
    } = useCart();
    
    if (cartItems.length === 0) {
        return (
            <div className="container mx-auto p-4">
                <h1 className="text-2xl font-bold mb-6">Your Cart</h1>
                <div className="bg-gray-100 p-6 rounded-lg text-center">
                    <p className="mb-4">Your cart is empty.</p>
                    <Link to="/" className="text-blue-500 hover:underline">
                        Start Shopping
                    </Link>
                </div>
            </div>
        );
    }
    
    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-6">Your Cart</h1>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="md:col-span-2">
                    <div className="bg-white shadow-md rounded-lg overflow-hidden">
                        <table className="w-full">
                            <thead className="bg-gray-50">
                                <tr>
                                    <th className="py-3 px-4 text-left">Product</th>
                                    <th className="py-3 px-4 text-center">Quantity</th>
                                    <th className="py-3 px-4 text-right">Price</th>
                                    <th className="py-3 px-4 text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-gray-200">
                                {cartItems.map(item => (
                                    <tr key={item.product_id}>
                                        <td className="py-4 px-4">
                                            <div className="flex items-center">
                                                <img 
                                                    src={item.image} 
                                                    alt={item.title} 
                                                    className="w-16 h-16 object-cover rounded" 
                                                />
                                                <div className="ml-4">
                                                    <p className="font-medium">{item.title}</p>
                                                    <p className="text-sm text-gray-500">{item.brand_name}</p>
                                                </div>
                                            </div>
                                        </td>
                                        <td className="py-4 px-4">
                                            <div className="flex justify-center items-center">
                                                <button 
                                                    className="w-8 h-8 bg-gray-200 rounded-l-md flex items-center justify-center"
                                                    onClick={() => updateQuantity(item.product_id, item.quantity - 1)}
                                                >
                                                    -
                                                </button>
                                                <span className="w-10 text-center">{item.quantity}</span>
                                                <button 
                                                    className="w-8 h-8 bg-gray-200 rounded-r-md flex items-center justify-center"
                                                    onClick={() => updateQuantity(item.product_id, item.quantity + 1)}
                                                >
                                                    +
                                                </button>
                                            </div>
                                        </td>
                                        <td className="py-4 px-4 text-right">
                                            ${(item.price * item.quantity).toFixed(2)}
                                        </td>
                                        <td className="py-4 px-4 text-right">
                                            <button 
                                                className="text-red-500 hover:text-red-700"
                                                onClick={() => removeFromCart(item.product_id)}
                                            >
                                                Remove
                                            </button>
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <div>
                    <div className="bg-white shadow-md rounded-lg p-6">
                        <h2 className="text-lg font-semibold mb-4">Order Summary</h2>
                        
                        <div className="space-y-3">
                            <div className="flex justify-between">
                                <span>Subtotal</span>
                                <span>${cartTotal.toFixed(2)}</span>
                            </div>
                            <div className="flex justify-between">
                                <span>Shipping</span>
                                <span>FREE</span>
                            </div>
                            <div className="border-t pt-3 mt-3">
                                <div className="flex justify-between font-semibold">
                                    <span>Total</span>
                                    <span>${cartTotal.toFixed(2)}</span>
                                </div>
                            </div>
                        </div>
                        
                        <button
                            className="mt-6 w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
                            onClick={proceedToCheckout}
                        >
                            Proceed to Checkout
                        </button>
                        
                        <div className="mt-4 text-center">
                            <Link to="/" className="text-blue-500 hover:underline">
                                Continue Shopping
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CartPage;
```

### Updated CartContext.jsx

```jsx
import React, { createContext, useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const CartContext = createContext();

export const useCart = () => useContext(CartContext);

export const CartProvider = ({ children }) => {
    const [cartItems, setCartItems] = useState([]);
    const [cartTotal, setCartTotal] = useState(0);
    const navigate = useNavigate();
    
    // Calculate total whenever cart changes
    useEffect(() => {
        const total = cartItems.reduce((sum, item) => sum + (item.price * item.quantity), 0);
        setCartTotal(total);
    }, [cartItems]);
    
    // Load cart from localStorage on initial load
    useEffect(() => {
        const savedCart = localStorage.getItem('cart');
        if (savedCart) {
            setCartItems(JSON.parse(savedCart));
        }
    }, []);
    
    // Save cart to localStorage whenever it changes
    useEffect(() => {
        localStorage.setItem('cart', JSON.stringify(cartItems));
    }, [cartItems]);
    
    // Add item to cart
    const addToCart = (product, quantity = 1) => {
        setCartItems(prevItems => {
            const existingItemIndex = prevItems.findIndex(item => item.product_id === product.product_id);
            
            if (existingItemIndex >= 0) {
                // Item exists, update quantity
                const updatedItems = [...prevItems];
                updatedItems[existingItemIndex] = {
                    ...updatedItems[existingItemIndex],
                    quantity: updatedItems[existingItemIndex].quantity + quantity
                };
                return updatedItems;
            } else {
                // Item doesn't exist, add new
                return [...prevItems, { ...product, quantity }];
            }
        });
    };
    
    // Remove item from cart
    const removeFromCart = (productId) => {
        setCartItems(prevItems => prevItems.filter(item => item.product_id !== productId));
    };
    
    // Update item quantity
    const updateQuantity = (productId, quantity) => {
        if (quantity <= 0) {
            removeFromCart(productId);
            return;
        }
        
        setCartItems(prevItems => 
            prevItems.map(item => 
                item.product_id === productId ? { ...item, quantity } : item
            )
        );
    };
    
    // Clear cart
    const clearCart = () => {
        setCartItems([]);
    };
    
    // Proceed to checkout
    const proceedToCheckout = () => {
        if (cartItems.length === 0) {
            alert('Your cart is empty');
            return;
        }
        
        navigate('/checkout');
    };