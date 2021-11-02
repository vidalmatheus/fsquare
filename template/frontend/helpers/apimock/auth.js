import { zuck } from './db/users'
import { mockasync } from './mockutils'

export default {
  login (username, password) {
    return mockasync({
      authenticated: true,
      user: zuck
    }).then(response => response.data)
  },
  logout () {
    return mockasync({}).then(response => response.data)
  },
  whoami () {
    return mockasync({
      authenticated: true,
      user: zuck
    }).then(response => response.data)
  }
}
