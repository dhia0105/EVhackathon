# Dockerfile

# Use Node.js image for building
FROM node:18 as build-stage

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app source
COPY . .

# Build the Vue.js application
RUN npm run build
EXPOSE 5173
# Start Nginx
CMD ["npm", "run", "dev"]
