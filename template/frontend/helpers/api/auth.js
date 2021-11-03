import { get, post } from './ajaxutils'

export default {
  login (username, password) {
    return post('/api/login', { username, password })
  },
  logout () {
    return post('/api/logout')
  },
  whoami () {
    return get('/api/whoami')
  }
}
