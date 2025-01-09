<template>
    <div class="create-post-page">
      <h1>Create a New Post</h1>
      <form @submit.prevent="createPost">
        <input 
          v-model="title" 
          placeholder="Title" 
          required 
        />
        <textarea 
          v-model="content" 
          placeholder="Write your post here..." 
          required
        ></textarea>
        <button type="submit" >Submit</button>
      </form>
      <router-link to="/" class="back-home-link">← Back to Home</router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
          title: '',
          content: ''
        
      };
    },
    methods: {
      async createPost() {
        try {
          // Send POST request to backend (replace with your actual backend URL)
          const response = await axios.post("http://localhost:8000/post", {
            title: this.title,
            content: this.content
          });
          console.log(response);
          // Handle the response and display the result
          this.error = null; // Clear any previous errors
        } catch (err) {
          // Handle any errors that occur during the request
          this.result = null; // Clear previous results
          this.error = 'Something went wrong. Please try again later.';
        }
         // Redirect to Home Page
         this.$router.push('/');
      }
    }
  };
  </script>
  
  <style scoped>
  .create-post-page {
    max-width: 600px;
    margin: 20px auto;
    text-align: center;
  }
  
  h1 {
    color: #42b983;
  }
  
  form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 20px auto;
  }
  
  input,
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #369870;
  }
  
  .back-home-link {
    display: inline-block;
    margin-top: 20px;
    text-decoration: none;
    color: #42b983;
  }
  </style>
  