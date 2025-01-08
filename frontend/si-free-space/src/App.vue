<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/" class="nav-link">🏠 Home</router-link>
        <router-link to="/create-post" class="nav-link">➕ Create Post</router-link>
        <router-link to="/submit-info" class="nav-link">🔍 Recommendations</router-link> <!-- New Link -->
      </nav>
    </header>

    <main>
      <router-view />
    </main>

    <footer>
      <p>&copy; {{ currentYear }} Sector initiatives Ecovadis. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentYear: new Date().getFullYear()
    };
  }
};
</script>

<style>
/* Same styles as before */
</style>
