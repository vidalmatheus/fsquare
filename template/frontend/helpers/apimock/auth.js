import { zuck } from './db/users'
import { mockasync } from './mockutils'

let keepLoggedIn = true

export default {
  login (username, password) {
    return mockasync(zuck)
  },
  logout () {
    keepLoggedIn = false
    return mockasync({})
  },
  whoami () {
    return mockasync({
      authenticated: keepLoggedIn,
      user: zuck
    })
  }
}
