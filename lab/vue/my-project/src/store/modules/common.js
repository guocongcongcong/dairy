const common = {
  state: {
    isCollapse: null
  },
  mutations: {
    toggleSiderBar (state) {
      state.isCollapse = !state.isCollapse
    }
  }
}

export default common
