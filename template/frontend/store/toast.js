export const state = () => ({
  opened: false,
  message: '',
  color: '',
  timeout: 6000,
  animationDuration: 500,
  timeoutFn: null
})

export const mutations = {
  open (state, data) {
    state.opened = true
    state.message = data.message
    state.color = data.color
    state.timeout = data.timeout || state.timeout
    state.animationDuration = data.animationDuration || state.animationDuration

    clearTimeout(state.timeoutFn)

    state.timeoutFn = setTimeout(() => {
      this.commit('toast/close')
    }, state.timeout)
  },
  close (state) {
    state.opened = false

    setTimeout(() => {
      this.commit('toast/clean')
    }, state.animationDuration)
  },
  clean (state) {
    state.message = ''
    state.color = ''
  }
}

export default {
  namespaced: true,
  state,
  mutations
}
