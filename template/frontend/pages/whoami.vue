<template>
  <v-container>
    <pre>loggedIn: {{ loggedIn }}</pre>
    <pre>{{ currentUserJson }}</pre>
  </v-container>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  computed: {
    currentUser () {
      return this.$store.state.auth
    },
    currentUserJson () {
      return JSON.stringify(this.currentUser, null, 2)
    },
    loggedIn () {
      return this.$store.getters['auth/loggedIn']
    }
  }
}
</script>
