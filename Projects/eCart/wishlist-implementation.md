# E-commerce Wishlist Feature Implementation Guide

## Table of Contents
1. [Overview](#overview)
2. [Implementation Steps](#implementation-steps)
3. [Database Schema](#database-schema)
4. [Backend Implementation](#backend-implementation)
   - [WishlistModel.js](#wishlistmodeljs)
   - [WishlistService.js](#wishlistservicejs)
   - [WishlistController.js](#wishlistcontrollerjs)
   - [wishlistRoutes.js](#wishlistroutesjs)
5. [Frontend Implementation](#frontend-implementation)
   - [WishlistContext.jsx](#wishlistcontextjsx)
   - [WishlistPage.jsx](#wishlistpagejsx)
   - [WishlistButton.jsx](#wishlistbuttonjsx)
   - [ProductCard.jsx Update](#productcardjsx-update)
   - [App.jsx Update](#appjsx-update)
6. [Testing](#testing)
7. [Navigation Integration](#navigation-integration)
8. [Product Detail Page Integration](#product-detail-page-integration)

## Overview

The wishlist feature allows authenticated users to save products they're interested in for future reference. This guide outlines the complete implementation for both backend and frontend components, designed to integrate seamlessly with your existing architecture.

## Implementation Steps

1. Create database tables for wishlists
2. Implement backend models, services, and controllers
3. Create API endpoints for wishlist operations
4. Develop frontend context provider for wishlist state management
5. Build wishlist page and components
6. Add wishlist toggle buttons to product cards
7. Update App.jsx with new routes

## Database Schema

Add the following table to your database schema:

```sql
-- Create the wishlist table
CREATE TABLE IF NOT EXISTS wishlists (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(uid) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, product_id)
);

-- Add index for faster querying
CREATE INDEX IF NOT EXISTS idx_wishlists_user_id ON wishlists(user_id);
```

## Backend Implementation

### WishlistModel.js

```javascript
/**
 * @file This file contains the WishlistModel class which is responsible for handling 
 * all the database queries related to the wishlists table.
 */

import { pool } from '../config/database.js';

class WishlistModel {
    /**
     * Get all wishlist items for a specific user
     * 
     * @param {string} userId - The user's ID
     * @returns {Promise<Array>} - Array of wishlist items with product details
     */
    static async getWishlistByUserId(userId) {
        const query = `
            SELECT w.id as wishlist_id, w.user_id, w.created_at, 
                   p.id as product_id, p.title, p.price, p.image, p.description,
                   b.name as brand_name, c.name as category_name
            FROM wishlists w
            JOIN product_details p ON w.product_id = p.product_id
            LEFT JOIN brands b ON p.brand_id = b.id
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE w.user_id = $1
            ORDER BY w.created_at DESC;
        `;
        
        try {
            const result = await pool.query(query, [userId]);
            return result.rows;
        } catch (error) {
            console.error('Error fetching wishlist items:', error.message);
            throw new Error('Database error: Failed to retrieve wishlist items');
        }
    }

    /**
     * Add a product to user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @param {number} productId - The product's ID
     * @returns {Promise<Object>} - The created wishlist item
     */
    static async addToWishlist(userId, productId) {
        const query = `
            INSERT INTO wishlists (user_id, product_id)
            VALUES ($1, $2)
            ON CONFLICT (user_id, product_id) DO NOTHING
            RETURNING *;
        `;
        
        try {
            const result = await pool.query(query, [userId, productId]);
            return result.rows[0];
        } catch (error) {
            console.error('Error adding to wishlist:', error.message);
            throw new Error('Database error: Failed to add item to wishlist');
        }
    }

    /**
     * Remove a product from user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @param {number} productId - The product's ID
     * @returns {Promise<boolean>} - True if removed successfully
     */
    static async removeFromWishlist(userId, productId) {
        const query = `
            DELETE FROM wishlists
            WHERE user_id = $1 AND product_id = $2
            RETURNING *;
        `;
        
        try {
            const result = await pool.query(query, [userId, productId]);
            return result.rows.length > 0;
        } catch (error) {
            console.error('Error removing from wishlist:', error.message);
            throw new Error('Database error: Failed to remove item from wishlist');
        }
    }

    /**
     * Check if a product is in user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @param {number} productId - The product's ID
     * @returns {Promise<boolean>} - True if product is in wishlist
     */
    static async isInWishlist(userId, productId) {
        const query = `
            SELECT EXISTS(
                SELECT 1 FROM wishlists
                WHERE user_id = $1 AND product_id = $2
            );
        `;
        
        try {
            const result = await pool.query(query, [userId, productId]);
            return result.rows[0].exists;
        } catch (error) {
            console.error('Error checking wishlist status:', error.message);
            throw new Error('Database error: Failed to check wishlist status');
        }
    }

    /**
     * Clear all items from user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @returns {Promise<boolean>} - True if cleared successfully
     */
    static async clearWishlist(userId) {
        const query = `
            DELETE FROM wishlists
            WHERE user_id = $1
            RETURNING *;
        `;
        
        try {
            const result = await pool.query(query, [userId]);
            return result.rowCount > 0;
        } catch (error) {
            console.error('Error clearing wishlist:', error.message);
            throw new Error('Database error: Failed to clear wishlist');
        }
    }
}

export default WishlistModel;
```

### WishlistService.js

```javascript
import WishlistModel from '../models/WishlistModel.js';

class WishlistService {
    /**
     * Get all wishlist items for a user
     * 
     * @param {string} userId - The user's ID
     * @returns {Promise<Array>} - Array of wishlist items
     */
    async getWishlistByUserId(userId) {
        try {
            return await WishlistModel.getWishlistByUserId(userId);
        } catch (error) {
            console.error('WishlistService.getWishlistByUserId(): Error:', error.message);
            throw error;
        }
    }

    /**
     * Add a product to user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @param {number} productId - The product's ID
     * @returns {Promise<Object>} - The created wishlist item
     */
    async addToWishlist(userId, productId) {
        try {
            return await WishlistModel.addToWishlist(userId, productId);
        } catch (error) {
            console.error('WishlistService.addToWishlist(): Error:', error.message);
            throw error;
        }
    }

    /**
     * Remove a product from user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @param {number} productId - The product's ID
     * @returns {Promise<boolean>} - True if removed successfully
     */
    async removeFromWishlist(userId, productId) {
        try {
            return await WishlistModel.removeFromWishlist(userId, productId);
        } catch (error) {
            console.error('WishlistService.removeFromWishlist(): Error:', error.message);
            throw error;
        }
    }

    /**
     * Check if a product is in user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @param {number} productId - The product's ID
     * @returns {Promise<boolean>} - True if product is in wishlist
     */
    async isInWishlist(userId, productId) {
        try {
            return await WishlistModel.isInWishlist(userId, productId);
        } catch (error) {
            console.error('WishlistService.isInWishlist(): Error:', error.message);
            throw error;
        }
    }

    /**
     * Clear all items from user's wishlist
     * 
     * @param {string} userId - The user's ID
     * @returns {Promise<boolean>} - True if cleared successfully
     */
    async clearWishlist(userId) {
        try {
            return await WishlistModel.clearWishlist(userId);
        } catch (error) {
            console.error('WishlistService.clearWishlist(): Error:', error.message);
            throw error;
        }
    }
}

// Export as a singleton
export default new WishlistService();
```

### WishlistController.js

```javascript
import WishlistService from '../services/WishlistService.js';

class WishlistController {
    /**
     * Get all wishlist items for a user
     * 
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     */
    static async getWishlistByUserId(req, res) {
        const { userId } = req.params;
        
        try {
            const wishlistItems = await WishlistService.getWishlistByUserId(userId);
            res.status(200).json(wishlistItems);
        } catch (error) {
            console.error('Error fetching wishlist:', error.message);
            res.status(500).json({ message: 'Failed to retrieve wishlist items' });
        }
    }

    /**
     * Add a product to user's wishlist
     * 
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     */
    static async addToWishlist(req, res) {
        const { userId, productId } = req.body;
        
        if (!userId || !productId) {
            return res.status(400).json({ message: 'User ID and Product ID are required' });
        }
        
        try {
            const wishlistItem = await WishlistService.addToWishlist(userId, productId);
            
            if (!wishlistItem) {
                return res.status(200).json({ message: 'Item already in wishlist' });
            }
            
            res.status(201).json(wishlistItem);
        } catch (error) {
            console.error('Error adding to wishlist:', error.message);
            res.status(500).json({ message: 'Failed to add item to wishlist' });
        }
    }

    /**
     * Remove a product from user's wishlist
     * 
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     */
    static async removeFromWishlist(req, res) {
        const { userId, productId } = req.params;
        
        try {
            const removed = await WishlistService.removeFromWishlist(userId, productId);
            
            if (!removed) {
                return res.status(404).json({ message: 'Item not found in wishlist' });
            }
            
            res.status(200).json({ message: 'Item removed from wishlist' });
        } catch (error) {
            console.error('Error removing from wishlist:', error.message);
            res.status(500).json({ message: 'Failed to remove item from wishlist' });
        }
    }

    /**
     * Check if a product is in user's wishlist
     * 
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     */
    static async isInWishlist(req, res) {
        const { userId, productId } = req.params;
        
        try {
            const isInWishlist = await WishlistService.isInWishlist(userId, productId);
            res.status(200).json({ isInWishlist });
        } catch (error) {
            console.error('Error checking wishlist status:', error.message);
            res.status(500).json({ message: 'Failed to check wishlist status' });
        }
    }

    /**
     * Clear all items from user's wishlist
     * 
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     */
    static async clearWishlist(req, res) {
        const { userId } = req.params;
        
        try {
            const cleared = await WishlistService.clearWishlist(userId);
            
            if (!cleared) {
                return res.status(200).json({ message: 'Wishlist is already empty' });
            }
            
            res.status(200).json({ message: 'Wishlist cleared successfully' });
        } catch (error) {
            console.error('Error clearing wishlist:', error.message);
            res.status(500).json({ message: 'Failed to clear wishlist' });
        }
    }
}

export default WishlistController;
```

### wishlistRoutes.js

```javascript
import express from 'express';
import WishlistController from '../controllers/WishlistController.js';

const router = express.Router();

// Get all wishlist items for a user
router.get('/user/:userId', WishlistController.getWishlistByUserId);

// Add a product to user's wishlist
router.post('/', WishlistController.addToWishlist);

// Remove a product from user's wishlist
router.delete('/user/:userId/product/:productId', WishlistController.removeFromWishlist);

// Check if a product is in user's wishlist
router.get('/user/:userId/product/:productId', WishlistController.isInWishlist);

// Clear all items from user's wishlist
router.delete('/user/:userId', WishlistController.clearWishlist);

export default router;
```

Add the wishlist routes to your main routes file:

```javascript
// In your index.js or server.js
import wishlistRoutes from './routes/wishlistRoutes.js';

// Add this with your other routes
app.use('/api/wishlist', wishlistRoutes);
```

## Frontend Implementation

### WishlistContext.jsx

```jsx
import React, { createContext, useState, useContext, useEffect } from 'react';
import { useAuth } from './AuthContext';
import { API_BASE_URL } from '../config/constants';

const WishlistContext = createContext();

export const useWishlist = () => useContext(WishlistContext);

export const WishlistProvider = ({ children }) => {
    const { user } = useAuth();
    const [wishlistItems, setWishlistItems] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    
    // Fetch wishlist when user changes
    useEffect(() => {
        if (user) {
            fetchWishlist();
        } else {
            setWishlistItems([]);
        }
    }, [user]);
    
    // Fetch user's wishlist
    const fetchWishlist = async () => {
        if (!user) return;
        
        setLoading(true);
        try {
            const response = await fetch(`${API_BASE_URL}/api/wishlist/user/${user.uid}`);
            
            if (!response.ok) {
                throw new Error('Failed to fetch wishlist');
            }
            
            const data = await response.json();
            setWishlistItems(data);
            setError(null);
        } catch (err) {
            console.error('Error fetching wishlist:', err);
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };
    
    // Add item to wishlist
    const addToWishlist = async (productId) => {
        if (!user) return false;
        
        try {
            const response = await fetch(`${API_BASE_URL}/api/wishlist`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    userId: user.uid,
                    productId,
                }),
            });
            
            if (!response.ok) {
                throw new Error('Failed to add to wishlist');
            }
            
            // Refresh wishlist
            fetchWishlist();
            return true;
        } catch (err) {
            console.error('Error adding to wishlist:', err);
            setError(err.message);
            return false;
        }
    };
    
    // Remove item from wishlist
    const removeFromWishlist = async (productId) => {
        if (!user) return false;
        
        try {
            const response = await fetch(`${API_BASE_URL}/api/wishlist/user/${user.uid}/product/${productId}`, {
                method: 'DELETE',
            });
            
            if (!response.ok) {
                throw new Error('Failed to remove from wishlist');
            }
            
            // Update local state instead of re-fetching
            setWishlistItems(prevItems => 
                prevItems.filter(item => item.product_id !== productId)
            );
            
            return true;
        } catch (err) {
            console.error('Error removing from wishlist:', err);
            setError(err.message);
            return false;
        }
    };
    
    // Check if product is in wishlist
    const isInWishlist = (productId) => {
        return wishlistItems.some(item => item.product_id === productId);
    };
    
    // Toggle wishlist item
    const toggleWishlistItem = async (productId) => {
        if (isInWishlist(productId)) {
            return await removeFromWishlist(productId);
        } else {
            return await addToWishlist(productId);
        }
    };
    
    // Clear wishlist
    const clearWishlist = async () => {
        if (!user) return false;
        
        try {
            const response = await fetch(`${API_BASE_URL}/api/wishlist/user/${user.uid}`, {
                method: 'DELETE',
            });
            
            if (!response.ok) {
                throw new Error('Failed to clear wishlist');
            }
            
            setWishlistItems([]);
            return true;
        } catch (err) {
            console.error('Error clearing wishlist:', err);
            setError(err.message);
            return false;
        }
    };
    
    return (
        <WishlistContext.Provider
            value={{
                wishlistItems,
                loading,
                error,
                addToWishlist,
                removeFromWishlist,
                isInWishlist,
                toggleWishlistItem,
                clearWishlist,
                refreshWishlist: fetchWishlist,
            }}
        >
            {children}
        </WishlistContext.Provider>
    );
};
```

### WishlistPage.jsx

```jsx
import React from 'react';
import { Link } from 'react-router-dom';
import { useWishlist } from '../context/WishlistContext';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';
import ProductCard from '../components/ProductCard';

const WishlistPage = () => {
    const { user } = useAuth();
    const { wishlistItems, loading, error, removeFromWishlist, clearWishlist } = useWishlist();
    const { addToCart } = useCart();
    
    // Handle moving item to cart
    const handleMoveToCart = (product) => {
        addToCart(product, 1);
        removeFromWishlist(product.product_id);
    };
    
    if (!user) {
        return (
            <div className="container mx-auto p-4">
                <h