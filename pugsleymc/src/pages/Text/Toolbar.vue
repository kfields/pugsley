<template>
  <q-toolbar>
    <q-btn
      flat
      dense
      round
      @click="$router.go(-1)"
    >
      <q-icon name="mdi-chevron-left" />
    </q-btn>
  </q-toolbar>
</template>

<script>
import UiMixin from 'src/mixins/ui'
export default {
  name: 'BasicToolbar',
  mixins: [ UiMixin ],
  props: [],
  components: {
  },
  methods: {
    goBack () {
      this.$router.go(-1)
    }
  }
}
</script>
