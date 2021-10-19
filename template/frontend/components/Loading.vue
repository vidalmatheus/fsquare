<template>
  <div>
    <v-layout :justify-center="center">
      <v-progress-circular
        indeterminate
        :size="size"
        color="secondary"
      />
    </v-layout>
    <p class="mt-2 text-xs-center">
      {{ title }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: ''
    },
    center: {
      type: String,
      default: 'center'
    },
    size: {
      type: Number,
      default: 50
    }
  }
}
</script>
