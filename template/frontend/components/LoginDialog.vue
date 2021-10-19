<template>
  <v-dialog v-model="visible" max-width="500px">
    <v-card>
      <v-card-title>Login</v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-text-field
            v-model="username"
            required
            label="Username"
          />
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            required
            @keyup.enter="login()"
          />
          <small
            v-if="error"
            style="color: red"
          >
            Wrong user or password
          </small>
        </v-container>
      </v-card-text>
      <v-btn
        class="blue--text darken-1"
        text
        @click="close()"
      >
        Cancel
      </v-btn>
      <v-btn
        class="blue--text darken-1"
        text
        :disabled="loading"
        :loading="loading"
        @click="login()"
      >
        Login
      </v-btn>
    </v-card>
  </v-dialog>
</template>

<script>
import api from '~api'

export default {
  data () {
    return {
      visible: false,
      loading: false,
      username: '',
      password: '',
      error: false
    }
  },
  methods: {
    open () {
      this.visible = true
    },
    close () {
      this.visible = false
    },
    login () {
      this.loading = true
      this.error = false
      api.auth.login(this.username, this.password).then(res => {
        const user = res.user
        const authenticated = res.authenticated
        if (user && authenticated) {
          this.$store.commit('auth/setCurrentUser', res)
          this.$store.commit('toast/open', {
            message: 'Welcome to your f-square app!',
            color: 'blue'
          })
          this.visible = false
        } else {
          this.error = true
        }
        this.loading = false
      })
    }
  }
}
</script>
