<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated reveal>
      <div v-bind:is="toolbar" />
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { UiMixin, LayoutMixin } from 'src/mixins'
export default {
  name: 'MyLayout',
  mixins: [ UiMixin, LayoutMixin ],
  data () {
    return {
    }
  },
  computed: {
  },
  methods: {
  },
  mounted () {
  }
}
</script>

<style>
</style>
