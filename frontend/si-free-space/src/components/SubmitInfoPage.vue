<template>
    <div class="submit-info-page">
      <h1>Together for Sustainability recommendations page</h1>
      <img :src="require('@/assets/tfs.png')" alt="Local Example" />
      <form @submit.prevent="submitInfo">
        <label for="question">Request a recommendation :</label>
        <input type="text" v-model="question" id="info" placeholder="Type something..." required />
        <button type="submit">Submit</button>
      </form>
  
      <div v-if="result" class="result">
        <h3>Result:</h3>
        <pre>{{ result }}</pre>
      </div>
  
      <div v-if="error" class="error">
        <h3>Error:</h3>
        <p>{{ error }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        question: '', // The user input
        sectorInitiative: 'tfs',
        result: null, // The result from the backend
        error: null // Error message if the request fails
      };
    },
    methods: {
      async submitInfo() {
        try {
          // Send POST request to backend (replace with your actual backend URL)
          const response = await axios.post("http://localhost:8000/ask", {
            question: this.question,
            sectorInitiative: this.sectorInitiative

          });
          console.log(response);
          // Handle the response and display the result
          this.result = response.data.recommendations;
          this.error = null; // Clear any previous errors
        } catch (err) {
          // Handle any errors that occur during the request
          this.result = null; // Clear previous results
          this.error = 'Something went wrong. Please try again later.';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .submit-info-page {
    max-width: 600px;
    margin: 20px auto;
    text-align: center;
  }
  
  form {
    margin-bottom: 20px;
  }
  
  input {
    padding: 8px;
    margin: 10px 0;
    width: 80%;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  
  button {
    padding: 8px 12px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #369870;
  }
  
  .result, .error {
    margin-top: 20px;
    padding: 15px;
    border-radius: 5px;
  }
  
  .result {
  background-color: #e7f7e7;
  border: 1px solid 
          #e7f7e7;
  }
  
  .error {
    background-color: #f8d7da;
    border: 1px solid #f5c6cb;
    color: #721c24;
  }
  </style>
  