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
      password: ''
    }
  },
  methods: {
    open () {
      this.visible = true
    },
    close () {
      this.visible = false
    },
    async login () {
      this.loading = true
      try {
        const res = await api.auth.login(this.username, this.password)
        const err = res.error || res.warning
        if (err) {
          this.$store.commit('toast/open', {
            message: err,
            color: res.error ? 'error' : 'warning'
          })
          return
        }
        if (res) {
          this.$store.commit('auth/setCurrentUser', res)
          this.$store.commit('toast/open', {
            message: `Welcome, ${res.first_name || res.username}!`,
            color: 'blue'
          })
          this.visible = false
        }
      } catch (err) {
        this.$store.commit('toast/open', {
          message: err,
          color: 'error'
        })
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
