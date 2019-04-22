<template>
  <div>
    <toolbar></toolbar>
    <editor-content class="editor__content" :editor="myeditor" />
  </div>
</template>

<script>
import { UiMixin, PageMixin } from 'src/mixins'
import Toolbar from 'components/HtmlEditToolbar'
import { Editor, EditorContent } from 'tiptap'
import {
  Blockquote,
  CodeBlock,
  HardBreak,
  Heading,
  HorizontalRule,
  OrderedList,
  BulletList,
  ListItem,
  TodoItem,
  TodoList,
  Bold,
  Code,
  Italic,
  Link,
  Strike,
  Underline,
  History
} from 'tiptap-extensions'

export default {
  mixins: [ UiMixin, PageMixin ],
  props: ['content'],
  components: {
    Toolbar,
    EditorContent
  },
  data () {
    return {
      myeditor: new Editor({
        extensions: [
          new Blockquote(),
          new BulletList(),
          new CodeBlock(),
          new HardBreak(),
          new Heading({ levels: [1, 2, 3] }),
          new HorizontalRule(),
          new ListItem(),
          new OrderedList(),
          new TodoItem(),
          new TodoList(),
          new Bold(),
          new Code(),
          new Italic(),
          new Link(),
          new Strike(),
          new Underline(),
          new History()
        ],
        content: this.content
      })
    }
  },
  mounted () {
  },
  beforeDestroy () {
    this.myeditor.destroy()
  },
  methods: {
  }
}
</script>
