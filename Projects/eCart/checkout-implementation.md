# Complete E-commerce Checkout & Order Processing Implementation Guide

Now that you've updated your database schema with the necessary tables for orders, order items, and shipping information, this guide will walk you through the complete implementation of the checkout flow.

## Table of Contents
1. [Backend Implementation](#backend-implementation)
   - [PaymentService.js](#paymentservicejs)
   - [OrderService.js Changes](#orderservicejs-changes)
   - [OrderController.js Updates](#ordercontrollerjs-updates)
2. [Frontend Implementation](#frontend-implementation)
   - [CartContext.jsx](#cartcontextjsx)
   - [CartPage.jsx](#cartpagejsx)
   - [CheckoutPage.jsx](#checkoutpagejsx)
   - [PaymentForm.jsx](#paymentformjsx)
   - [OrderConfirmationPage.jsx](#orderconfirmationpagejsx)
   - [OrdersPage.jsx](#orderspagejsx)
3. [Route Updates](#route-updates)
   - [App.jsx Updates](#appjsx-updates)
4. [Stripe Configuration](#stripe-configuration)
5. [Testing](#testing)

## Backend Implementation

### PaymentService.js

Create a new file `services/PaymentService.js`:

```javascript
// services/PaymentService.js
import Stripe from 'stripe';
import dotenv from 'dotenv';

dotenv.config();

// Initialize Stripe with your secret key (from .env file)
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY);

class PaymentService {
    // Create a PaymentIntent for the order
    async createPaymentIntent(amount) {
        try {
            const paymentIntent = await stripe.paymentIntents.create({
                amount: Math.round(amount * 100), // Convert to cents
                currency: 'usd',
                payment_method_types: ['card'],
            });
            
            return {
                clientSecret: paymentIntent.client_secret,
                stripePaymentId: paymentIntent.id
            };
        } catch (error) {
            console.error("❌ Error creating payment intent:", error.message);
            throw new Error("Payment processing error: " + error.message);
        }
    }
}

export default new PaymentService();
```

### OrderService.js Changes

Update your `services/OrderService.js` to add the shipping info functionality:

```javascript
// services/OrderService.js
import OrderModel from '../models/OrderModel.js'; 
import PaymentService from './PaymentService.js';
import { pool } from '../config/database.js';

class OrderService {
    // Create a new order and generate a PaymentIntent
    async createOrder(userId, orderItems, shippingInfo) {
        const client = await pool.connect();
        try {
            await client.query("BEGIN");

            // Step 1: Calculate total price
            const totalPrice = this.calculateTotalPrice(orderItems);

            // Step 2: Create a PaymentIntent with Stripe
            const { clientSecret, stripePaymentId } = await PaymentService.createPaymentIntent(totalPrice);

            // Step 3: Create a new order in the database (initially 'pending')
            const order = await OrderModel.createOrder(userId, totalPrice, "pending", stripePaymentId);
            const orderId = order.id;

            // Step 4: Add items to the order
            await OrderModel.addOrderItems(orderId, orderItems);

            // Step 5: Store shipping information
            if (shippingInfo) {
                await this.saveShippingInfo(orderId, userId, shippingInfo);
            }

            await client.query("COMMIT");
            return { order, clientSecret }; // Send clientSecret to frontend
        } catch (error) {
            await client.query("ROLLBACK");
            console.error("❌ OrderService.createOrder(): Error:", error.message);
            throw new Error("Order creation failed: " + error.message);
        } finally {
            client.release();
        }
    }

    // Save shipping information
    async saveShippingInfo(orderId, userId, shippingInfo) {
        const query = `
            INSERT INTO shipping_info (order_id, user_id, name, address, city, state, zip, email)
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
            RETURNING *;
        `;
        
        const values = [
            orderId, 
            userId, 
            shippingInfo.name,
            shippingInfo.address,
            shippingInfo.city,
            shippingInfo.state,
            shippingInfo.zip,
            shippingInfo.email
        ];
        
        try {
            const result = await pool.query(query, values);
            return result.rows[0];
        } catch (error) {
            console.error("Error saving shipping info:", error.message);
            throw new Error("Failed to save shipping information");
        }
    }

    // Keep your existing methods:
    // - confirmPayment
    // - calculateTotalPrice
    // - getOrderById
    // - getOrdersByUserId
    // - updateOrderStatus
    // - deleteOrder
    // - getAllOrders
}

// Export as a single instance
export default new OrderService();
```

### OrderController.js Updates

Make sure your controller is ready to receive shipping info:

```javascript
// controllers/OrderController.js
static async createOrder(req, res) {
    try {
        const { userId, orderItems, shippingInfo } = req.body;
        
        // Validate input
        if (!userId || !orderItems || orderItems.length === 0) {
            return res.status(400).json({ error: 'Invalid order data' });
        }
        
        const order = await OrderService.createOrder(userId, orderItems, shippingInfo);
        res.status(201).json(order);
    } catch (error) {
        console.log("OrderController.createOrder(): Error:", error.message);
        res.status(500).json({ error: error.message });
    }
}
```

## Frontend Implementation

### CartContext.jsx

Create or update your CartContext:

```jsx
// context/CartContext.jsx
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
    
    return (
        <CartContext.Provider value={{
            cartItems,
            cartTotal,
            addToCart,
            removeFromCart,
            updateQuantity,
            clearCart,
            proceedToCheckout
        }}>
            {children}
        </CartContext.Provider>
    );
};
```

### CartPage.jsx

Create a CartPage component:

```jsx
// pages/CartPage.jsx
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
                            onClick={proceedToCheckout}
                            className="mt-6 w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
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

### CheckoutPage.jsx

Create a CheckoutPage component:

```jsx
// pages/CheckoutPage.jsx
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
        email: user?.email || ''
    });
    
    const [orderCreated, setOrderCreated] = useState(false);
    const [orderId, setOrderId] = useState(null);
    
    // Redirect to login if not authenticated
    useEffect(() => {
        if (!user) {
            navigate('/login', { state: { from: '/checkout' } });
        }
    }, [user, navigate]);
    
    // Redirect to cart if cart is empty
    useEffect(() => {
        if (cartItems.length === 0 && !orderCreated) {
            navigate('/cart');
        }
    }, [cartItems, navigate, orderCreated]);
    
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
    
    if (!user || (cartItems.length === 0 && !orderCreated)) {
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

### PaymentForm.jsx

Update your PaymentForm component:

```jsx
// components/PaymentForm.jsx
import React, { useState } from "react";
import { useStripe, useElements, CardElement } from "@stripe/react-stripe-js";
import { API_BASE_URL } from "../config/constants"; // Make sure you have this file

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
        
        // Validate shipping info
        for (const [key, value] of Object.entries(shippingInfo)) {
            if (!value) {
                setErrorMessage(`Please fill in your ${key.replace(/([A-Z])/g, ' $1').toLowerCase()}`);
                return;
            }
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

Create an OrderConfirmationPage component:

```jsx
// pages/OrderConfirmationPage.jsx
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
                
                {/* Shipping Info */}
                {order[0].shipping_name && (
                    <div className="mt-4 pt-3 border-t">
                        <h3 className="text-lg font-medium mb-2">Shipping Information</h3>
                        <p>{order[0].shipping_name}</p>
                        <p>{order[0].shipping_address}</p>
                        <p>{order[0].shipping_city}, {order[0].shipping_state} {order[0].shipping_zip}</p>
                        <p>{order[0].shipping_email}</p>
                    </div>
                )}
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

Update your OrdersPage component:

```jsx
// pages/OrdersPage.jsx
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/