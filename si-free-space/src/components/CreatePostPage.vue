<template>
    <div class="create-post-page">
      <h1>Create a New Post</h1>
      <form @submit.prevent="submitPost">
        <input 
          v-model="newPost.title" 
          placeholder="Title" 
          required 
        />
        <textarea 
          v-model="newPost.content" 
          placeholder="Write your post here..." 
          required
        ></textarea>
        <button type="submit">Submit</button>
      </form>
      <router-link to="/" class="back-home-link">← Back to Home</router-link>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newPost: {
          title: '',
          content: ''
        }
      };
    },
    methods: {
      submitPost() {
        if (!this.newPost.title || !this.newPost.content) return;
  
        // Save to local storage or mock backend (temporary example)
        const posts = JSON.parse(localStorage.getItem('posts')) || [];
        posts.push({
          title: this.newPost.title,
          content: this.newPost.content
        });
        localStorage.setItem('posts', JSON.stringify(posts));
  
        // Clear the form
        this.newPost.title = '';
        this.newPost.content = '';
  
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
  