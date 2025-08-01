# E-commerce Sorting and Filtering Optimization Guide
#### Note: See the separate Checkout and Order Processing Guide for checkout functionality

## Table of Contents
1. [Backend Changes](#backend-changes)
   - [ProductModel.js Updates](#productmodeljs-updates)
   - [ProductService.js Updates](#productservicejs-updates)
   - [ProductController.js Updates](#productcontrollerjs-updates)
   - [Route Updates](#route-updates)
   - [Database Optimizations](#database-optimizations)
2. [Frontend Changes](#frontend-changes)
   - [ProductContext.jsx Updates](#productcontextjsx-updates)
   - [Frontend Service Updates](#frontend-service-updates)
   - [New UI Components](#new-ui-components)
   - [ProductPage.jsx Updates](#productpagejsx-updates)
3. [Implementation Steps](#implementation-steps)

## Backend Changes

### ProductModel.js Updates

Add a new method to fetch category with filter options:

```javascript
static async getProductsByCategoryWithFilterOptions(category) {
    const selectQuery = `
        SELECT 
            category_name,
            COUNT(*) as product_count,
            array_agg(DISTINCT sizes) as available_sizes,
            array_agg(DISTINCT colors) as available_colors,
            array_agg(DISTINCT conditions) as available_conditions,
            MIN(price) as min_price,
            MAX(price) as max_price
        FROM product_details
        WHERE category_name ILIKE $1
        GROUP BY category_name;
    `;

    try {
        const categoryResults = await pool.query(selectQuery, [category.trim()]);
        
        // Get all products in this category
        const productsQuery = `
            SELECT * 
            FROM product_details
            WHERE category_name ILIKE $1
            ORDER BY title;
        `;
        
        const productsResults = await pool.query(productsQuery, [category.trim()]);
        
        // Return both category metadata and products
        return {
            ...categoryResults.rows[0],
            products: productsResults.rows
        };
    } catch (error) {
        console.error("Error fetching category with filter options:", error.message);
        throw new Error("Database query failed.");
    }
}
```

Simplify the existing filtering method:

```javascript
static async getProductsByFilters(category, filters = {}, sortBy = 'title', sortOrder = 'ASC') {
    // Start with basic query
    let selectQuery = 'SELECT * FROM product_details WHERE 1=1';
    const queryParams = [];
    let paramIndex = 1;
    
    // Add category filter if provided
    if (category) {
        selectQuery += ` AND category_name ILIKE $${paramIndex}`;
        queryParams.push(category.trim());
        paramIndex++;
    }
    
    // Add size filter if provided
    const { size, color, condition, minPrice, maxPrice } = filters;
    
    if (size) { 
        selectQuery += ` AND $${paramIndex} = ANY (sizes)`;
        queryParams.push(size);
        paramIndex++;
    }
    
    if (color) {
        selectQuery += ` AND $${paramIndex} = ANY (colors)`;
        queryParams.push(color);
        paramIndex++;
    }
    
    if (condition) {
        selectQuery += ` AND $${paramIndex} = ANY (conditions)`;
        queryParams.push(condition);
        paramIndex++;
    }
    
    // Add price range filters
    if (minPrice !== undefined && minPrice !== null) {
        selectQuery += ` AND price >= $${paramIndex}`;
        queryParams.push(parseFloat(minPrice));
        paramIndex++;
    }
    
    if (maxPrice !== undefined && maxPrice !== null) {
        selectQuery += ` AND price <= $${paramIndex}`;
        queryParams.push(parseFloat(maxPrice));
        paramIndex++;
    }
    
    // Add sorting
    // Validate sortBy to prevent SQL injection
    const validSortFields = ['title', 'price', 'created_at', 'brand_name'];
    const validSortBy = validSortFields.includes(sortBy) ? sortBy : 'title';
    
    // Validate sortOrder to prevent SQL injection
    const validSortOrder = ['ASC', 'DESC'].includes(sortOrder) ? sortOrder : 'ASC';
    
    selectQuery += ` ORDER BY ${validSortBy} ${validSortOrder}`;
    
    try {
        const results = await pool.query(selectQuery, queryParams);
        return results.rows;
    } catch (error) {
        console.error("Error fetching products with filters:", error.message);
        throw new Error("Database query failed.");
    }
}
```

### ProductService.js Updates

```javascript
async getProductsByCategoryWithFilterOptions(category) {
    try {
        return await ProductModel.getProductsByCategoryWithFilterOptions(category);
    } catch (error) {
        console.error('ProductService.getProductsByCategoryWithFilterOptions(): Error:', error.message);
        throw error;
    }
}

async getProductsByFilters(category, filters = {}, sortBy = 'title', sortOrder = 'ASC') {
    try {
        return await ProductModel.getProductsByFilters(category, filters, sortBy, sortOrder);
    } catch (error) {
        console.error('ProductService.getProductsByFilters(): Error:', error.message);
        throw error;
    }
}
```

### ProductController.js Updates

```javascript
static async getProductsByCategory(req, res) {
    const productService = new ProductService();
    const { category } = req.params;
    const { withFilterOptions } = req.query;
    
    try {
        if (withFilterOptions === 'true') {
            // Get category with available filter options
            const data = await productService.getProductsByCategoryWithFilterOptions(category);
            res.status(200).json(data);
        } else {
            // Just get products in this category
            const products = await productService.getProductsByCategory(category);
            res.status(200).json(products);
        }
    } catch (error) {
        console.error("Error fetching products by category:", error);
        res.status(500).json({ message: "Failed to retrieve products" });
    }
}

static async getProductsByFilters(req, res) {
    const productService = new ProductService();
    const { category } = req.params; // May be undefined for global filtering
    const { 
        size, 
        color, 
        condition, 
        minPrice, 
        maxPrice, 
        sortBy = 'title', 
        sortOrder = 'ASC' 
    } = req.query;
    
    try {
        const filters = {
            size,
            color,
            condition,
            minPrice,
            maxPrice
        };
        
        const products = await productService.getProductsByFilters(
            category,
            filters,
            sortBy,
            sortOrder
        );
        
        res.status(200).json(products);
    } catch (error) {
        console.error("Error filtering products:", error);
        res.status(500).json({ message: "Failed to retrieve filtered products" });
    }
}
```

### Route Updates

```javascript
// routes/productRoutes.js
import express from 'express';
import ProductController from '../controllers/ProductController.js';

const router = express.Router();

// Get all products
router.get('/', ProductController.getAllProducts);

// Get a product by ID
router.get('/:id', ProductController.getProductById);

// Get products by category with optional filter options
router.get('/category/:category', ProductController.getProductsByCategory);

// Get filtered products within a category
router.get('/category/:category/filter', ProductController.getProductsByFilters);

// Global filter endpoint (no category)
router.get('/filter', ProductController.getProductsByFilters);

// Search products by title
router.get('/search', ProductController.searchProductsByTitle);

// CRUD operations
router.post('/', ProductController.addProduct);
router.put('/:id', ProductController.updateProduct);
router.delete('/:id', ProductController.deleteProduct);

export default router;
```

### Database Optimizations

Add these to your database schema to improve performance:

```sql
-- Add indexes to improve filter performance
CREATE INDEX IF NOT EXISTS idx_product_details_category_name ON product_details(category_name);
CREATE INDEX IF NOT EXISTS idx_product_details_price ON product_details(price);
CREATE INDEX IF NOT EXISTS idx_product_details_created_at ON product_details(created_at);
```

## Frontend Changes

### ProductContext.jsx Updates

```jsx
import React, { createContext, useState, useContext, useEffect } from "react";
import productsService from "../services/productService";

const ProductContext = createContext();

export const useProductContext = () => useContext(ProductContext);

export const ProductProvider = ({ children }) => {
    // State variables 
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [selectedCategory, setSelectedCategory] = useState('');
    const [availableFilters, setAvailableFilters] = useState({
        sizes: [],
        colors: [],
        conditions: [],
        minPrice: 0,
        maxPrice: 1000
    });
    const [activeFilters, setActiveFilters] = useState({
        size: '',
        color: '',
        condition: '',
        minPrice: 0,
        maxPrice: 1000
    });
    const [sortBy, setSortBy] = useState('title');
    const [sortOrder, setSortOrder] = useState('ASC');

    // Helper function to extract unique values from an array of arrays
    const extractUniqueValues = (items, property) => {
        const allValues = [];
        items.forEach(item => {
            if (Array.isArray(item[property])) {
                item[property].forEach(value => {
                    if (value && !allValues.includes(value)) {
                        allValues.push(value);
                    }
                });
            }
        });
        return allValues;
    };

    // Fetch all products (used when no category is selected)
    const fetchAllProducts = async () => {
        setLoading(true);
        try {
            const data = await productsService.fetchAllProducts();
            setProducts(data);
            
            // Extract available filter options from all products
            setAvailableFilters({
                sizes: extractUniqueValues(data, 'sizes'),
                colors: extractUniqueValues(data, 'colors'),
                conditions: extractUniqueValues(data, 'conditions'),
                minPrice: Math.min(...data.map(p => p.price)),
                maxPrice: Math.max(...data.map(p => p.price))
            });
            
            setError(null);
        } catch (err) {
            setError(err.message);
            console.error("Error fetching all products:", err);
        } finally {
            setLoading(false);
        }
    };

    // Fetch category with available filter options
    const fetchCategoryWithFilters = async (category) => {
        setLoading(true);
        try {
            const data = await productsService.fetchCategoryWithFilterOptions(category);
            setProducts(data.products);
            
            // Set available filter options from category data
            setAvailableFilters({
                sizes: data.available_sizes || [],
                colors: data.available_colors || [],
                conditions: data.available_conditions || [],
                minPrice: data.min_price || 0,
                maxPrice: data.max_price || 1000
            });
            
            setError(null);
        } catch (err) {
            setError(err.message);
            console.error("Error fetching category with filters:", err);
        } finally {
            setLoading(false);
        }
    };

    // Apply filters to current category
    const applyFilters = async () => {
        setLoading(true);
        try {
            const data = await productsService.fetchFilteredProducts(
                selectedCategory,
                {
                    ...activeFilters,
                    minPrice: activeFilters.minPrice || 0,
                    maxPrice: activeFilters.maxPrice || 1000
                },
                sortBy,
                sortOrder
            );
            setProducts(data);
            setError(null);
        } catch (err) {
            setError(err.message);
            console.error("Error applying filters:", err);
        } finally {
            setLoading(false);
        }
    };

    // Select a category
    const selectCategory = (category) => {
        setSelectedCategory(category);
        resetFilters();
    };

    // Update a single filter
    const updateFilter = (filterName, value) => {
        setActiveFilters(prev => ({
            ...prev,
            [filterName]: value
        }));
    };

    // Update price range
    const updatePriceRange = (min, max) => {
        setActiveFilters(prev => ({
            ...prev,
            minPrice: min,
            maxPrice: max
        }));
    };

    // Reset all filters but keep category
    const resetFilters = () => {
        setActiveFilters({
            size: '',
            color: '',
            condition: '',
            minPrice: 0,
            maxPrice: availableFilters.maxPrice || 1000
        });
    };

    // Update sorting
    const updateSorting = (field, order) => {
        setSortBy(field);
        setSortOrder(order);
    };

    // Load initial data and when category changes
    useEffect(() => {
        if (selectedCategory) {
            fetchCategoryWithFilters(selectedCategory);
        } else {
            fetchAllProducts();
        }
    }, [selectedCategory]);

    // Apply filters when sorting changes
    useEffect(() => {
        if (products.length > 0) {
            applyFilters();
        }
    }, [sortBy, sortOrder]);

    return (
        <ProductContext.Provider
            value={{
                products,
                loading,
                error,
                selectedCategory,
                availableFilters,
                activeFilters,
                sortBy,
                sortOrder,
                selectCategory,
                updateFilter,
                updatePriceRange,
                resetFilters,
                updateSorting,
                applyFilters
            }}
        >
            {children}
        </ProductContext.Provider>
    );
};
```

### Frontend Service Updates

```javascript
// productService.js
async fetchCategoryWithFilterOptions(category) {
    try {
        const response = await fetch(`${API_BASE_URL}/api/products/category/${encodeURIComponent(category)}?withFilterOptions=true`);
        if (!response.ok) {
            throw new Error("HTTP error: " + response.status);
        }
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error fetching category with filters:", error);
        throw error;
    }
}

async fetchFilteredProducts(category, filters = {}, sortBy = 'title', sortOrder = 'ASC') {
    try { 
        // Build query parameters 
        const params = new URLSearchParams(); 

        // Add filter parameters
        Object.entries(filters).forEach(([key, value]) => {
            if (value !== undefined && value !== null && value !== '') {
                params.append(key, value); 
            }
        });

        // Add sorting parameters 
        params.append('sortBy', sortBy);
        params.append('sortOrder', sortOrder);

        // API request - different endpoint based on whether category is provided
        const url = category 
            ? `${API_BASE_URL}/api/products/category/${encodeURIComponent(category)}/filter?${params.toString()}`
            : `${API_BASE_URL}/api/products/filter?${params.toString()}`;
            
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("HTTP error: " + response.status);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error fetching filtered products:", error);
        throw error;
    }
}
```

### New UI Components

#### CategorySidebar.jsx

```jsx
import React, { useState, useEffect } from "react";
import { useProductContext } from "../context/ProductContext";
import categoryService from "../services/categoryService";

export default function CategorySidebar() {
    const { selectedCategory, selectCategory } = useProductContext();
    const [categories, setCategories] = useState([]);
    const [isOpen, setIsOpen] = useState(false);
    
    // Fetch categories
    useEffect(() => {
        const fetchCategories = async () => {
            try {
                const data = await categoryService.fetchAllCategories();
                setCategories(data);
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        };
        fetchCategories();
    }, []);

    // Toggle mobile dropdown
    const toggleDropdown = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className="w-full md:w-60 p-3 border-black/10 text-xs">
            <button
                onClick={toggleDropdown}
                className="bg-blue-500 text-white px-4 py-2 rounded mb-4 md:hidden text-xs"
            >
                {isOpen ? "Hide Categories" : "Show Categories"}
            </button>

            <div className={`${isOpen ? "block" : "hidden"} md:block`}>
                <h2 className="text-xs font-semibold mb-4">CATEGORIES</h2>
                
                <ul className="mt-2">
                    <li className="flex items-center mb-2">
                        <input 
                            type="radio" 
                            id="category-all" 
                            name="category"
                            value=""
                            className="w-3 h-3"
                            checked={selectedCategory === ''}
                            onChange={() => selectCategory('')}
                        />
                        <label htmlFor="category-all" className="ml-2">All Categories</label>
                    </li>
                    {categories.map((category) => (
                        <li key={category.id} className="flex items-center mb-2">
                            <input 
                                type="radio" 
                                id={`category-${category.id}`} 
                                name="category"
                                value={category.name}
                                className="w-3 h-3"
                                checked={selectedCategory === category.name}
                                onChange={() => selectCategory(category.name)}
                            />
                            <label htmlFor={`category-${category.id}`} className="ml-2">{category.name}</label>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}
```

#### FilterControls.jsx

```jsx
import React, { useState, useEffect } from "react";
import { useProductContext } from "../context/ProductContext";

export default function FilterControls() {
    const { 
        availableFilters,
        activeFilters,
        updateFilter,
        updatePriceRange,
        resetFilters,
        applyFilters,
        updateSorting,
        loading
    } = useProductContext();
    
    const [currentPriceMax, setCurrentPriceMax] = useState(activeFilters.maxPrice);
    const [expandedSections, setExpandedSections] = useState({
        sizes: true,
        colors: true,
        conditions: true,
        price: true
    });
    
    // Update price slider when available filters change
    useEffect(() => {
        setCurrentPriceMax(activeFilters.maxPrice);
    }, [activeFilters.maxPrice]);
    
    // Handle price range change
    const handlePriceChange = (e) => {
        setCurrentPriceMax(parseInt(e.target.value));
    };
    
    // Apply price filter
    const applyPriceRange = () => {
        updatePriceRange(activeFilters.minPrice, currentPriceMax);
    };
    
    // Handle sort change
    const handleSortChange = (e) => {
        const [field, order] = e.target.value.split('-');
        updateSorting(field, order.toUpperCase());
    };
    
    // Toggle sections
    const toggleSection = (section) => {
        setExpandedSections(prev => ({
            ...prev,
            [section]: !prev[section]
        }));
    };
    
    return (
        <div className="bg-gray-50 p-4 rounded-md mb-4">
            <div className="flex justify-between items-center mb-4">
                <h3 className="font-medium">Filter & Sort</h3>
                <button 
                    onClick={resetFilters}
                    className="text-blue-500 text-xs hover:underline"
                    disabled={loading}
                >
                    Reset Filters
                </button>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {/* Sort By */}
                <div>
                    <label className="block mb-2 text-sm font-medium">Sort By</label>
                    <select
                        className="w-full border rounded p-2 text-sm"
                        onChange={handleSortChange}
                        defaultValue="title-asc"
                        disabled={loading}
                    >
                        <option value="title-asc">Name (A-Z)</option>
                        <option value="title-desc">Name (Z-A)</option>
                        <option value="price-asc">Price (Low to High)</option>
                        <option value="price-desc">Price (High to Low)</option>
                        <option value="created_at-desc">Newest</option>
                    </select>
                </div>
                
                {/* Size Filter */}
                <div>
                    <div 
                        className="flex justify-between items-center cursor-pointer mb-2" 
                        onClick={() => toggleSection('sizes')}
                    >
                        <label className="text-sm font-medium">Size</label>
                        <span>{expandedSections.sizes ? '−' : '+'}</span>
                    </div>
                    
                    {expandedSections.sizes && (
                        <select 
                            className="w-full border rounded p-2 text-sm"
                            value={activeFilters.size}
                            onChange={(e) => updateFilter('size', e.target.value)}
                            disabled={loading}
                        >
                            <option value="">All Sizes</option>
                            {availableFilters.sizes.map(size => (
                                <option key={size} value={size}>{size}</option>
                            ))}
                        </select>
                    )}
                </div>
                
                {/* Color Filter */}
                <div>
                    <div 
                        className="flex justify-between items-center cursor-pointer mb-2" 
                        onClick={() => toggleSection('colors')}
                    >
                        <label className="text-sm font-medium">Color</label>
                        <span>{expandedSections.colors ? '−' : '+'}</span>
                    </div>
                    
                    {expandedSections.colors && (
                        <select 
                            className="w-full border rounded p-2 text-sm"
                            value={activeFilters.color}
                            onChange={(e) => updateFilter('color', e.target.value)}
                            disabled={loading}
                        >
                            <option value="">All Colors</option>
                            {availableFilters.colors.map(color => (
                                <option key={color} value={color}>{color}</option>
                            ))}
                        </select>
                    )}
                </div>
                
                {/* Condition Filter */}
                <div>
                    <div 
                        className="flex justify-between items-center cursor-pointer mb-2" 
                        onClick={() => toggleSection('conditions')}
                    >
                        <label className="text-sm font-medium">Condition</label>
                        <span>{expandedSections.conditions ? '−' : '+'}</span>
                    </div>
                    
                    {expandedSections.conditions && (
                        <select 
                            className="w-full border rounded p-2 text-sm"
                            value={activeFilters.condition}
                            onChange={(e) => updateFilter('condition', e.target.value)}
                            disabled={loading}
                        >
                            <option value="">All Conditions</option>
                            {availableFilters.conditions.map(condition => (
                                <option key={condition} value={condition}>{condition}</option>
                            ))}
                        </select>
                    )}
                </div>
            </div>
            
            {/* Price Range */}
            <div className="mt-4">
                <div 
                    className="flex justify-between items-center cursor-pointer mb-2" 
                    onClick={() => toggleSection('price')}
                >
                    <label className="text-sm font-medium">Price Range</label>
                    <span>{expandedSections.price ? '−' : '+'}</span>
                </div>
                
                {expandedSections.price && (
                    <>
                        <div className="flex justify-between items-center mb-2">
                            <span className="text-xs">${activeFilters.minPrice}</span>
                            <span className="text-xs">${currentPriceMax}</span>
                        </div>
                        <input 
                            type="range" 
                            min={activeFilters.minPrice} 
                            max={availableFilters.maxPrice || 1000} 
                            value={currentPriceMax}
                            onChange={handlePriceChange}
                            onMouseUp={applyPriceRange}
                            onTouchEnd={applyPriceRange}
                            className="w-full"
                            disabled={loading}
                        />
                    </>
                )}
            </div>
            
            {/* Apply Button */}
            <button 
                onClick={applyFilters}
                className="mt-4 bg-blue-500 text-white px-4 py-2 rounded text-sm w-full"
                disabled={loading}
            >
                {loading ? 'Applying...' : 'Apply Filters'}
            </button>
        </div>
    );
}
```

### ProductPage.jsx Updates

```jsx
import React from 'react';
import CategorySidebar from '../components/CategorySidebar';
import FilterControls from '../components/FilterControls';
import ProductGrid from '../components/ProductGrid';
import { useProductContext } from '../context/ProductContext';

const ProductPage = () => {
    const { selectedCategory, products, loading } = useProductContext();
    
    return (
        <div className="container mx-auto px-4 py-8">
            <div className="flex flex-col md:flex-row gap-6">
                {/* Categories on the side */}
                <div className="md:w-1/4 lg:w-1/5">
                    <CategorySidebar />
                </div>
                
                <div className="flex-1">
                    {/* Product count and filtering info */}
                    <div className="mb-4">
                        <h1 className="text-2xl font-bold mb-2">
                            {selectedCategory ? selectedCategory : 'All Products'}
                        </h1>
                        <p className="text-sm text-gray-500">
                            {loading ? 'Loading...' : `Showing ${products.length} products`}
                        </p>
                    </div>
                    
                    {/* Filter controls */}
                    <FilterControls />
                    
                    {/* Product grid */}
                    <ProductGrid />
                </div>
            </div>
        </div>
    );
};

export default ProductPage;
```

## Implementation Steps

1. **Back-End Updates**:
   - Update `ProductModel.js` with the new methods
   - Modify `ProductService.js` to use these methods
   - Update `ProductController.js` with new controller actions
   - Create new routes in your router file

2. **Database Optimization**:
   - Add the recommended indexes to your database

3. **Front-End Updates**:
   - Update `productService.js` with new API methods
   - Replace the current `ProductContext.jsx` with the new version
   - Create the new UI components (`CategorySidebar.jsx` and `FilterControls.jsx`)
   - Update `ProductPage.jsx` to use these components

4. **Testing**:
   - Test category selection
   - Test filter application within a category
   - Test sorting functionality
   - Verify reset filters works correctly
   - Test mobile responsiveness

Following these steps will give you a clean separation between category selection and filtering, similar to eBay's approach, while keeping your codebase maintainable and performant.
