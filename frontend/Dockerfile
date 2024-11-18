# Use the official Node.js image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of your app's code
COPY . .

# Expose the port React will run on (default for React dev server is 3000)
EXPOSE 3000

# Run the development server
CMD ["npm", "run", "dev"]
