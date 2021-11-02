import axios from 'axios'

export async function get (url, params) {
  const resp = await axios.get(url, { params })
  return resp.data
}

export async function post (url, params) {
  const resp = await axios.post(url, params)
  return resp.data
}
