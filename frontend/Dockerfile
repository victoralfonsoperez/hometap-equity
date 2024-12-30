# Step 1: Build the React app using Node 20 and Vite
FROM node:20 AS build

# Set working directory inside container
WORKDIR /app

# Copy the rest of the application
COPY . .

# Install dependencies
RUN npm install

# Build the app using Vite (production build)
RUN npm run build

# Expose port for Vite to serve the app (default: 5173)
EXPOSE 5173

# Serve the app using Vite CLI in production mode
CMD ["npm", "run", "serve", "--port", "5173"]