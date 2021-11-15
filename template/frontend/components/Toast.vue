<template>
  <v-snackbar
    v-model="opened"
    :timeout="timeout"
    :color="color"
    rounded
    :transition="transition"
  >
    {{ message }}

    <template #action="{ on, attrs }">
      <v-btn
        dark
        text
        v-bind="attrs"
        v-on="on"
        @click="close"
      >
        Fechar
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
export default {
  computed: {
    opened () {
      return this.$store && this.$store.state.toast.opened
    },
    message () {
      return this.$store.state.toast.message
    },
    timeout () {
      return this.$store.state.toast.timeout || 6000
    },
    color () {
      return this.$store.state.toast.color
    },
    transition () {
      return this.opened ? 'scroll-y-reverse-transition' : 'scroll-y-transition'
    }
  },
  methods: {
    close () {
      this.$store.commit('toast/close')
    }
  }
}
</script>
