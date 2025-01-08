<template>
    <div class="posts-page">
      <h1>Published Posts</h1>
      <div v-if="posts.length">
        <div v-for="(post, index) in posts" :key="index" class="post">
          <h3>{{ post.title }}</h3>
          <p>{{ post.content }}</p>
        </div>
      </div>
      <div v-else>
        <p>No posts available yet.</p>
      </div>
      <router-link to="/">Go Back Home</router-link>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        posts: [
          { title: 'First Post', content: 'This is the first post content.' },
          { title: 'Second Post', content: 'This is the second post content.' }
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .posts-page {
    max-width: 600px;
    margin: 20px auto;
    text-align: center;
  }
  
  .post {
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ddd;
    border-radius: 8px;
    text-align: left;
  }
  
  .post h3 {
    margin: 0 0 5px;
    color: #42b983;
  }
  </style>
  