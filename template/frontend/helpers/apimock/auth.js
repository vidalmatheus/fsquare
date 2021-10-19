import { zuck } from './db/users'
import { mockasync } from './mockutils'

export default {
  login (username, password) {
    let loggedUser = {}
    if (username === 'mark' && password === '123') {
      loggedUser = zuck
    }
    return mockasync({
      authenticated: true,
      user: loggedUser
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
