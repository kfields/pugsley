<template>
  <q-page padding>
    <textarea ref="editor"></textarea>
  </q-page>
</template>

<script>
import { UiMixin, PageMixin } from 'src/mixins'
import Toolbar from './Toolbar'

import CodeMirror from 'codemirror'
import 'codemirror/lib/codemirror.css'
// import 'codemirror/theme/monokai.css'
// import 'codemirror/mode/javascript/javascript.js'
import 'codemirror/mode/xml/xml.js'

export default {
  mixins: [ UiMixin, PageMixin ],
  props: [],
  components: {
  },
  data () {
    return {
      myeditor: null
    }
  },
  mounted () {
    const myeditor = this.myeditor = CodeMirror.fromTextArea(this.$refs.editor, {
      theme: 'miakai',
      mode: 'xml',
      htmlMode: true,
      lineNumbers: true,
      styleActiveLine: true,
      matchBrackets: true,
      tabSize: 2
    })
    myeditor.setValue(this.edited.object[this.edited.prop])
  },
  beforeDestroy () {
    this.edited.object[this.edited.prop] = this.myeditor.getValue()
    // this.myeditor.destroy()
  },
  methods: {
    onSwitch () {
      this.setEditor(this.myeditor)
      this.setToolbar(Toolbar)
    }
  }
}
</script>
