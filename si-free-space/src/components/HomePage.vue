<template>
  <div class="home-page">
    <h1>Published Posts</h1>
    <router-link to="/create-post" class="create-post-link">
      ➕ Create a New Post
    </router-link>
    <section class="published-posts-section">
      <div v-if="posts.length">
        <div v-for="(post, index) in posts" :key="index" class="post">
          <h3>{{ post.title }}</h3>
          <p>{{ post.content }}</p>

          <!-- Comments Section -->
          <div class="comments-section">
            <h4>Comments:</h4>
            <div v-if="post.comments && post.comments.length">
              <ul>
                <li v-for="(comment, cIndex) in post.comments" :key="cIndex">
                  {{ comment }}
                </li>
              </ul>
            </div>
            <div v-else>
              <p>No comments yet. Be the first to comment!</p>
            </div>
            <!-- Add Comment Form -->
            <form @submit.prevent="addComment(index)">
              <input
                v-model="newComment[index]"
                placeholder="Add a comment"
                required
              />
              <button type="submit">Comment</button>
            </form>
          </div>
        </div>
      </div>
      <div v-else>
        <p>No posts available yet. Be the first to post!</p>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      posts: [],
      newComment: {} // Object to hold comments for each post
    };
  },
  async created() {
    // Load posts from local storage
    try {
          // Send POST request to backend (replace with your actual backend URL)
          const response = await axios.get("http://localhost:8000/posts", {
            question: this.question,
            sector_initiative: this.sectorInitiative

          });
          console.log(response);
          // Handle the response and display the result
          this.posts = response.data.posts;
          this.error = null; // Clear any previous errors
        } catch (err) {
          // Handle any errors that occur during the request
          this.result = null; // Clear previous results
          this.error = 'Something went wrong. Please try again later.';
        }
  },
  methods: {
    addComment(index) {
      if (!this.newComment[index]) return;

      // Ensure the comments array exists
      if (!this.posts[index].comments) {
        this.$set(this.posts[index], 'comments', []);
      }

      // Add the new comment
      this.posts[index].comments.push(this.newComment[index]);
      this.newComment[index] = ''; // Clear the input

      // Save updated posts to local storage
      localStorage.setItem('posts', JSON.stringify(this.posts));
    }
  }
};
</script>

<style scoped>
.home-page {
  max-width: 600px;
  margin: 20px auto;
  text-align: center;
}

h1 {
  color: #42b983;
}

.create-post-link {
  display: inline-block;
  margin: 10px 0 20px;
  text-decoration: none;
  background-color: #42b983;
  color: white;
  padding: 8px 12px;
  border-radius: 5px;
}

.published-posts-section .post {
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: left;
}

.published-posts-section .post h3 {
  margin: 0 0 5px;
  color: #42b983;
}

/* Comments Section */
.comments-section {
  margin-top: 10px;
  padding: 10px;
  border-top: 1px solid #ddd;
}

.comments-section h4 {
  margin: 0 0 5px;
}

.comments-section ul {
  list-style: none;
  padding: 0;
}

.comments-section li {
  margin: 5px 0;
  padding: 5px;
  background: #f4f4f4;
  border-radius: 5px;
}

.comments-section form {
  margin-top: 10px;
  display: flex;
  gap: 5px;
}

.comments-section input {
  flex: 1;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.comments-section button {
  padding: 5px 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.comments-section button:hover {
  background-color: #369870;
}
</style>
