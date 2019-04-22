import Toolbar from 'components/DefaultToolbar'

export default {
  mounted () {
    this.setPageTitle(this.title)
    this.onSwitch()
  },
  beforeRouteUpdate (to, from, next) {
    this.onSwitch()
    next()
  },
  methods: {
    onSwitch () {
      this.setToolbar(Toolbar)
    }
  }
}
