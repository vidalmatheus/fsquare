export function mockasync (data) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve(data), 600)
  })
}

export function mockasyncerror () {
  return new Promise((resolve, reject) => {
    setTimeout(() => reject(new Error('Something went wrong')), 600)
  })
}
