import { mapGetters, mapActions } from 'vuex'

export default {
  computed: {
    leftDrawerOpen: {
      get: function () {
        return this.$store.getters['leftDrawerOpen']
      },
      set: function (val) {
        this.$store.commit('setLeftDrawerOpen', val)
      }
    },
    ...mapGetters([
      'page',
      'pageTitle',
      'toolbar',
      'editor',
      'edited'
    ])
  },
  methods: {
    ...mapActions([
      'setPage',
      'setPageTitle',
      'setLeftDrawerOpen',
      'setToolbar',
      'setEditor',
      'setEdited'
    ])
  }
}
