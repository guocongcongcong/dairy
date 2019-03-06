# components

## 组件基础

```js
// 定义一个名为 button-counter 的新组件
Vue.component("button-counter", {
  data: function() {
    return {
      count: 0
    };
  },
  template:
    '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
});
```

---


### 组件注册

- **组件名**：直接在 DOM (即非字符串的模板) 中使用时只有 kebab-case 是有效的。
- **全局注册**：`Vue.component('component-a', { /* ... */ })`，这些组件是全局注册的。也就是说它们在注册之后可以用在任何新创建的 Vue 根实例 (new Vue) 的模板中。也就是说这三个组件在各自内部也都可以相互使用。
- **局部注册**:`var ComponentA = { /* ... */ }`,`...components: {'component-a': ComponentA,}...`.对于 components 对象中的每个属性来说，其属性名就是自定义元素的名字，其属性值就是这个组件的选项对象。注意局部注册的*组件在其子组件中不可用*。

---

### Prop(Prop 向子组件传递数据)

> Prop 是你可以在组件上注册的一些自定义特性。当一个值传递给一个 prop 特性的时候，它就变成了那个组件实例的一个属性。为了给博文组件传递一个标题，我们可以用一个 props 选项将其包含在该组件可接受的 prop 列表中：

```js
Vue.component("blog-post", {
  props: ["title"],
  template: "<h3>{{ title }}</h3>"
});
```

- **典型应用**:你会发现我们可以使用 v-bind 来动态传递 prop。这在你一开始不清楚要渲染的具体内容，比如从一个 API 获取博文列表的时候，是非常有用的。

```html
<blog-post
  v-for="post in posts"
  v-bind:key="post.id"
  v-bind:title="post.title"
></blog-post>
<script>
  new Vue({
    el: "#blog-post-demo",
    data: {
      posts: [
        { id: 1, title: "My journey with Vue" },
        { id: 2, title: "Blogging with Vue" },
        { id: 3, title: "Why Vue is so fun" }
      ]
    }
  });
</script>
```

- 当你使用 DOM 中的模板时，camelCase (驼峰命名法) 的 prop 名需要使用其等价的 kebab-case (短横线分隔命名) 命名。
- **Prop 的类型**：通常你希望每个 prop 都有指定的值类型。这时，你可以以对象形式列出 prop，这些属性的名称和值分别是 prop 各自的名称和类型：
```js
Vue.component("blog-post", {
  props: {
    title: String,
    likes: Number,
    isPublished: Boolean,
    commentIds: Array,
    author: Object
  },
  template: "<h3>{{ title }}</h3>"
});
//这一部分与组件类型检车和其他的prop的验证有关联
```
- **传递静态或动态的Prop**：`<blog-post title="My journey with Vue"></blog-post>`:静态，`<blog-post v-bind:title="post.title"></blog-post>`:动态。实际上任何类型的值都可以传给一个 prop。

- **数字/布尔值/数组/对象**
```html
<!-----------------------数组------------------------------>
<!-- 即便 `42` 是静态的，我们仍然需要 `v-bind` 来告诉 Vue -->
<!-- 这是一个 JavaScript 表达式而不是一个字符串。-->
<blog-post v-bind:likes="42"></blog-post>

<!-- 用一个变量进行动态赋值。-->
<blog-post v-bind:likes="post.likes"></blog-post>


<!-----------------------布尔值----------------------------->
<!-- 包含该 prop 没有值的情况在内，都意味着 `true`。-->
<blog-post is-published></blog-post>

<!-- 即便 `false` 是静态的，我们仍然需要 `v-bind` 来告诉 Vue -->
<!-- 这是一个 JavaScript 表达式而不是一个字符串。-->
<blog-post v-bind:is-published="false"></blog-post>

<!-- 用一个变量进行动态赋值。-->
<blog-post v-bind:is-published="post.isPublished"></blog-post>


<!-----------------------数组------------------------------>
<!-- 即便数组是静态的，我们仍然需要 `v-bind` 来告诉 Vue -->
<!-- 这是一个 JavaScript 表达式而不是一个字符串。-->
<blog-post v-bind:comment-ids="[234, 266, 273]"></blog-post>

<!-- 用一个变量进行动态赋值。-->
<blog-post v-bind:comment-ids="post.commentIds"></blog-post>


<!-----------------------对象------------------------------>
<!-- 即便对象是静态的，我们仍然需要 `v-bind` 来告诉 Vue -->
<!-- 这是一个 JavaScript 表达式而不是一个字符串。-->
<blog-post
  v-bind:author="{
    name: 'Veronica',
    company: 'Veridian Dynamics'
  }"
></blog-post>

<!-- 用一个变量进行动态赋值。-->
<blog-post v-bind:author="post.author"></blog-post>

```

- **对象的所有属性**:如果你想要将一个对象的所有属性都作为 prop 传入，你可以使用不带参数的 v-bind (取代 v-bind:prop-name)。例如，对于一个给定的对象 post。
```html
<!--                    对象的所有属性                   -->
<script>
post: {
  id: 1,
  title: 'My Journey with Vue'
}
</script>
<!-- 下面的模板： -->
<blog-post v-bind="post"></blog-post>
<!-- 等价于： -->
<blog-post
  v-bind:id="post.id"
  v-bind:title="post.title"
></blog-post>
```

- **单向数据流**:*单向下行绑定*,这意味着你不应该在一个子组件内部改变 prop
  1. *这个 prop 用来传递一个初始值；这个子组件接下来希望将其作为一个本地的 prop 数据来使用。* **在这种情况下，最好定义一个本地的 data 属性并将这个 prop 用作其初始值：**
        ```js
        props: ['initialCounter'],
        data: function () {
        return {
            counter: this.initialCounter
        }
        }
        ```

  2. *这个 prop 以一种原始的值传入且需要进行转换。* **在这种情况下，最好使用这个 prop 的值来定义一个计算属性：**
        ```js
        props: ['size'],
        computed: {
            normalizedSize: function () {
                return this.size.trim().toLowerCase()
            }
        }
        ```

- **Prop验证**：为了定制 prop 的验证方式，你可以为 props 中的值提供一个带有验证需求的对象，而不是一个字符串数组。额外的，type 还可以是一个自定义的构造函数，并且通过 instanceof 来进行检查确认。例如，给定下列现成的构造函数：来验证 author prop 的值是否是通过 new Person 创建的。
    ```js
    function Person (firstName, lastName) {
        this.firstName = firstName
        this.lastName = lastName
    }
    Vue.component('my-component', {
        props: {
            // 基础的类型检查 (`null` 和 `undefined` 会通过任何类型验证)
            propA: Number,
            // 多个可能的类型
            propB: [String, Number],
            // 必填的字符串
            propC: {
            type: String,
            required: true
            },
            // 带有默认值的数字
            propD: {
            type: Number,
            default: 100
            },
            // 带有默认值的对象
            propE: {
            type: Object,
            // 对象或数组默认值必须从一个工厂函数获取
            default: function () {
                return { message: 'hello' }
            }
            },
            // 自定义验证函数
            propF: {
            validator: function (value) {
                // 这个值必须匹配下列字符串中的一个
                return ['success', 'warning', 'danger'].indexOf(value) !== -1
            }
            },
            author: Person
        }
    })
    ```

### 模块系统

- 模块系统中局部注册
- 说明你使用了诸如 Babel 和 webpack 的模块系统。在这些情况下，我们推荐创建一个 components 目录，并将每个组件放置在其各自的文件中。

```js
import ComponentA from "./ComponentA";
import ComponentC from "./ComponentC";

export default {
  components: {
    ComponentA,
    ComponentC
  }
  // ...
};
```

- 基础组件的自动化全局注册
- 可能你的许多组件只是包裹了一个输入框或按钮之类的元素，是相对通用的。我们有时候会把它们称为基础组件，它们会在各个组件中被频繁的用到。

```html
<template>
  <BaseInput v-model="searchText" @keydown.enter="search" />
  <BaseButton @click="search">
    <BaseIcon name="search" />
  </BaseButton>
</template>
<script>
  import BaseButton from "./BaseButton.vue";
  import BaseIcon from "./BaseIcon.vue";
  import BaseInput from "./BaseInput.vue";

  export default {
    components: {
      BaseButton,
      BaseIcon,
      BaseInput
    }
  };
</script>
```
### 自定义事件

- **事件名**：不同于组件和 prop，事件名不存在任何自动化的大小写转换。而是触发的事件名需要完全匹配监听这个事件所用的名称。
  - 举个例子，如果触发一个 camelCase 名字的事件：`this.$emit('myEvent')`,则监听这个名字的 kebab-case 版本是不会有任何效果的：`<my-component v-on:my-event="doSomething"></my-component>`.
  - 不同于组件和 prop，事件名不会被用作一个 JavaScript 变量名或属性名，所以就没有理由使用 camelCase 或 PascalCase 了。并且 v-on 事件监听器在 DOM 模板中会被自动转换为全小写 (因为 HTML 是大小写不敏感的)，所以 v-on:myEvent 将会变成 v-on:myevent——导致 myEvent 不可能被监听到。
  - **因此，我们推荐你始终使用 kebab-case 的事件名。**

- **自定义组件的 v-model**:一个组件上的 v-model 默认会利用名为 value 的 prop 和名为 input 的事件，但是像单选框、复选框等类型的输入控件可能会将 value 特性用于不同的目的。model 选项可以用来避免这样的冲突：




### 插槽

- 除非子组件模板包含至少一个 <slot> 插口，否则父组件的内容将会被丢弃。当子组件模板只有一个没有属性的插槽时，父组件传入的整个内容片段将插入到插槽所在的 DOM 位置，并替换掉插槽标签本身。

### 动态组件&异步组件
- 你会注意到，如果你选择了一篇文章，切换到 Archive 标签，然后再切换回 Posts，是不会继续展示你之前选择的文章的。这是因为你每次切换新标签的时候，Vue 都创建了一个新的 currentTabComponent 实例。

>在动态组件上使用 keep-alive:

### 处理边界情况

- 这里记录的都是和处理边界情况有关的功能，即一些需要对 Vue 的规则做一些小调整的特殊情况。不过注意这些功能都是有劣势或危险的场景的。我们会在每个案例中注明，所以当你使用每个功能的时候请稍加留意。
