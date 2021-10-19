export const state = () => ({
  authenticated: false,
  currentUser: {}
})

export const mutations = {
  setCurrentUser (state, { user, authenticated }) {
    state.currentUser = user
    state.authenticated = authenticated
    console.log(state)

    if (user) {
      if (user.permissions === undefined) {
        user.permissions = {}
      }
    }
  },
  updateCurrentUser (state, props) {
    Object.assign(state.currentUser, props)
  },
  removeCurrentUser (state) {
    state.currentUser = null
  }
}

export const getters = {
  loggedIn (state) {
    return !!(
      state.currentUser &&
      state.authenticated &&
      state.currentUser.permissions
    )
  },
  userId (state) {
    return state.currentUser ? state.currentUser.id : null
  }
}
