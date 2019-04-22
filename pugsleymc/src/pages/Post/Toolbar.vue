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

    <q-toolbar-title>
      {{pageTitle}}
          <q-btn
      flat
      dense
      round
      @click="page.save()"
      aria-label="Save"
    >
      <q-icon name="save" />
    </q-btn>

    </q-toolbar-title>

  </q-toolbar>
</template>

<script>
import UiMixin from 'src/mixins/ui'
import { mapActions } from 'vuex'
export default {
  name: 'DefaultToolbar',
  mixins: [
    UiMixin
  ],
  props: [],
  methods: {
    ...mapActions([
      'toggleLeftDrawer'
    ])
  }
}
</script>
