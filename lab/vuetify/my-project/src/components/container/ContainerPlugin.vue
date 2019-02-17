<template>
  <v-container fluid grid-list-md>
    <v-layout row wrap v-for="(item,i) in items" :key="i">
      <v-flex xs12>
        <div v-if="i%2 == 0">
          <v-card dark color="primary">
            <v-card-text>
              <code>{{item.name}}</code>
              : {{item.content}}
              <br>
              <var>{{item.link}}</var>
            </v-card-text>
          </v-card>
        </div>
        <div v-else>
          <v-card dark color="secondary">
            <v-card-text>
              <code>{{item.name}}</code>
              : {{item.content}}
              <br>
              <var>{{item.link}}</var>
            </v-card-text>
          </v-card>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      items: [
        {
          name: "Grid",

          link: "https://next.vuetifyjs.com/zh-Hans/framework/grid",
          content:
            "Vuetify拥有一个12点的栅格系统，它使用flex-box构建，栅格用于布局应用程序的内容。它包含5种类型的媒体断点，用于定位特定的屏幕大小或方向。栅格组件的属性实际上是从它们定义的属性派生的类，这允许您轻松地将这些辅助类指定为属性，同时仍然提供在任何地方使用的类。"
        },
        {
          name: "v-container",

          link: "https://next.vuetifyjs.com/zh-Hans/framework/grid-lists",
          content:
            "栅格列表是v-container组件的一个插件，可以在项目之间添加沟槽控件。"
        },
        {
          name: "v-layout",
          link: "https://next.vuetifyjs.com/zh-Hans/framework/grid-lists",
          content: ""
        },
        {
          name: "v-flex",
          link: "https://next.vuetifyjs.com/zh-Hans/framework/grid-lists",
          content: ""
        },
        {
          name: "v-spacer",

          link: "https://next.vuetifyjs.com/zh-Hans/framework/grid-lists",
          content: ""
        },
        {
          name: "code var",

          link: "代码，变量",
          content: "https://next.vuetifyjs.com/zh-Hans/framework/content#-var"
        },
        {
          name: "v-alert",

          link: "https://next.vuetifyjs.com/zh-Hans/components/alerts",
          content:
            "组件被用来向用户传达重要信息，它有4个变种，成功（success），信息（info），警告（warning）和错误（error）。它们被分配了可以修改的表示不同操作的默认图标"
        },
        {
          name: "v-avatar",

          link: "https://next.vuetifyjs.com/zh-Hans/components/avatars",
          content:
            "组件被用来控制用于控制响应图像的大小和边界半径，通常用于显示个人介绍的图片。"
        },
        {
          name: "v-badge",

          link: "https://next.vuetifyjs.com/zh-Hans/components/badges",
          content:
            "组件可以包装任何类型的内容以突出显示用户的信息，或只提醒注意特定的元素。"
        },
        {
          name: "v-bottom-nav",

          link:
            "https://next.vuetifyjs.com/zh-Hans/components/bottom-navigation",
          content:
            "组件是一个侧边栏的替代方案。它主要用于移动端，并有两个变种，图标+文本和转变。"
        },
        {
          name: "v-bottom-sheet",

          link: "https://next.vuetifyjs.com/zh-Hans/components/bottom-sheets",
          content:
            "底部表单是一个修改后的v-dialog，可以从屏幕底部滑动，类似于一个v-bottom-nav。底部导航组件用于按钮和特定应用程序级别操作，而底部表单可以包含任何内容。"
        },
        {
          name: "v-breadcrumbs",

          link: "https://next.vuetifyjs.com/zh-Hans/components/breadcrumbs",
          content:
            "组件是一个页面导航辅助器。它可以接受一个Material Icons图标或字符作为分隔符。一个包含字段href，text和disabled的对象数组可以被传递给组件的items属性。此外，还有一个常规插槽用于更多地控制面包屑，可以使用v-breadcrumbs-item或者其它自定义标记。"
        },
        {
          name: "v-btn",

          link: "https://next.vuetifyjs.com/zh-Hans/components/buttons",
          content:
            "组件用一个material design主题和多个选项来替换标准的html按钮。任何色彩辅助类都可以用来改变背景或文字的颜色。"
        },
        {
          name: "v-speed-dial",

          link:
            "https://next.vuetifyjs.com/zh-Hans/components/floating-action-buttons",
          content:
            " <按钮: 悬浮响应按钮> v-btn组件可以用作悬浮响应按钮；它可以为应用提供最主要的操作。通过与v-speed-dial 组件的组合使用, 你可以为你的用户创建一系列的功能集。"
        },
        {
          name: "v-calendar",

          link: "https://next.vuetifyjs.com/zh-Hans/components/calendars",
          content:
            "The <code>v-calendar</code> component is used to display information in a daily, weekly, or monthly view. The daily view has slots for all day or timed elements, and the weekly and monthly view has a slot for each day. Optionally you can pass in an array of events and they will be rendered over the appropriate days and times."
        },
        {
          name: "v-card",

          link: "https://next.vuetifyjs.com/zh-Hans/components/cards",
          content:
            " <卡片> 一个多功能组件，可用于从面板到静态图像的任何事物。card组件有许多班助组件，使标记尽可能简单。没有列出选项的组件使用Vue的功能组件选项来加快渲染速度，并作为标记糖来使构建更容易。"
        },
        {
          name: "v-carousel",

          link: "https://next.vuetifyjs.com/zh-Hans/components/carousels",
          content: " <轮播> 组件用于在旋转的计时器上显示大量的可视内容"
        },
        {
          name: "v-chip",

          link: "https://next.vuetifyjs.com/zh-Hans/components/chips",
          content:
            " <后切薯条> 组件用于传递小块信息。使用close属性，厚切薯条变得互动，允许用户交互。"
        },
        {
          name: "v-data-iterator",

          link: "https://next.vuetifyjs.com/zh-Hans/components/data-iterator",
          content:
            " <数据迭代器> 组件用于显示数据，并将其大部分功能与v-data-table组件共享。功能包括排序、搜索、分页和选择。"
        },
        {
          name: "v-data-table ",

          link: "https://next.vuetifyjs.com/zh-Hans/components/data-tables",
          content:
            "用于显示表格数据，功能包括排序、搜索、分页、行内编辑、头部提示以及行选择"
        },
        {
          name: "v-dialog",

          link: "https://next.vuetifyjs.com/zh-Hans/components/dialogs",
          content:
            "组件用来通知用户有关特定任务的信息，并且可能包含重要信息，需要作出决定或者涉及多任务；应谨慎使用对话框，因为它是中断的。"
        },
        {
          name: "v-divider",

          link: "https://next.vuetifyjs.com/zh-Hans/components/dividers",
          content: " <分割线> 组件用来分隔列表的各部分"
        },
        {
          name: "v-expansion-panel",

          link:
            "https://next.vuetifyjs.com/zh-Hans/components/expansion-panels",
          content:
            " <扩展面板> 组件对于减少大量信息的垂直空间非常有用。该组件的默认功能是一次仅显示一个展开面板主题。但是使用<code>expandable</code>属性后，扩展面板会保持打开状态，直到被显式关闭。"
        },
        {
          name: "v-footer",

          link: "https://next.vuetifyjs.com/zh-Hans/components/footer",
          content: "用于显示用户可能希望从站点内的所有页面访问到的公共信息。"
        },
        {
          name: "v-btn-toggle",

          link: "https://next.vuetifyjs.com/zh-Hans/components/button-groups",
          content:
            "The v-btn-toggle component is a simple wrapper for v-item-group built specifically to work with v-btn."
        },
        {
          name: "v-window",

          link: "https://next.vuetifyjs.com/zh-Hans/components/windows",
          content:
            "The v-window component is the baseline functionality for transitioning content from 1 pane to another. Other components such as v-tabs, v-carousel and v-stepper utilize this component at their core."
        },
        {
          name: "v-icon",

          link:
            "https://next.vuetifyjs.com/zh-Hans/components/icons  https://material.io/tools/icons/",
          content:
            "组件提供了大量的字形来为应用程序的各个方面提供上下文。Vuetify图标利用Google的Material图标字体库。有关所有可用图标的列表，请访问官方的Material Icons页面。"
        },
        {
          name: "v-hover",

          link: "https://next.vuetifyjs.com/zh-Hans/components/hover",
          content:
            "The v-hover component provides a clean interface for handling hover states for any component."
        },
        {
          name: "v-img",

          link: "https://next.vuetifyjs.com/zh-Hans/components/images",
          content:
            "The v-img component is packed with features to support rich media. Combined with the vuetify-loader, you can add dynamic progressive images to provide a better user experience."
        },
        {
          name: "v-form",

          link: "https://next.vuetifyjs.com/zh-Hans/components/forms",
          content:
            "The internal v-form component makes it easy to add validation to form inputs. All input components have a rules prop which takes an array of functions. These functions allow you to specify conditions in which the field is valid or invalid. Whenever the value of an input is changed, each function in the array will receive the new value. If a function returns false or a string, validation has failed."
        },
        {
          name: "v-input",

          link: "https://next.vuetifyjs.com/zh-Hans/components/inputs",
          content:
            "The v-input component gives you a baseline to create your own custom inputs. It consists of a prepend/append slot, messages, and a default slot. It is recommended that you extend this component, but it can be used as a standalone."
        },
        {
          name: "v-select",

          link: "https://next.vuetifyjs.com/zh-Hans/components/selects",
          content: "选择器组件用于从选项列表中收集用户提供的信息。"
        },
        {
          name: "v-radio-group checkbox",

          link:
            "https://next.vuetifyjs.com/zh-Hans/components/selection-controls",
          content:
            "选择控制组件允许用户使用选择项，这些组件必须和 v-model 属性一起使用，因为他们无法保持自己的状态。"
        },
        {
          name: "v-textarea",

          link: "https://next.vuetifyjs.com/zh-Hans/components/textarea",
          content:
            "Textarea components are used for collecting large amounts of textual data."
        },
        {
          name: "v-text-field",

          link: "https://next.vuetifyjs.com/zh-Hans/components/text-fields",
          content: "文本框组件用于收集用户提供的信息。"
        },
        {
          name: "v-jumbotron",

          link: "https://next.vuetifyjs.com/zh-Hans/components/jumbotrons",
          content:
            "The jumbotron is a flexible call to action component. Supports background images, gradient overlays and much more."
        },
        {
          name: "v-list",

          link: "https://next.vuetifyjs.com/zh-Hans/components/lists",
          content:
            "组件用于显示信息，它可以包含一个头像、内容、操作、列表组标题等等。列表也可以包含子元素并在侧边栏（sidebar）使用。"
        },
        {
          name: "v-menu",

          link: "https://next.vuetifyjs.com/zh-Hans/components/menus",
          content: "组件展示一个菜单在用于激活它的元素的位置上。"
        },
        {
          name: "v-navigation-drawer",

          link:
            "https://next.vuetifyjs.com/zh-Hans/components/navigation-drawers",
          content:
            "组件是用户将用来浏览应用程序的内容，导航抽屉被预先配置为可以使用或不使用vue-router。"
        },
        {
          name: "v-pagination",

          link: "https://next.vuetifyjs.com/zh-Hans/components/paginations",
          content:
            " <分页> 组件用于分隔长的数据集，以便用户更容易地使用信息。根据提供的长度，分页组件将自动缩放。要维护当前页面，只需提供一个v-model标签。"
        },
        {
          name: "v-parallax",

          link: "",
          content: " <视差> 组件创建一个3d效果使图像显示比窗口滚动更慢。"
        },
        {
          name: "v-date-picker",

          link: "https://next.vuetifyjs.com/zh-Hans/components/date-pickers",
          content:
            "The v-date-picker is stand-alone component that can be utilized in many existing Vuetify components. It offers the user a visual representation for selecting date/month."
        },
        {
          name: "v-progress-circular v-progress-linear",

          link: "https://next.vuetifyjs.com/zh-Hans/components/progress",
          content:
            "组件用于将数据直观地传达给用户。他们也可以代表一个不确定的数量，如加载或处理。这些组件包含一个位于组件容器中心的插槽。"
        },
        {
          name: "v-rating",

          link: "https://next.vuetifyjs.com/zh-Hans/components/ratings",
          content:
            " <星标> The v-rating component provides a simple interface for gathering user feedback."
        },
        {
          name: "v-sheet",

          link: "https://next.vuetifyjs.com/zh-Hans/components/sheets",
          content:
            "The v-sheet is designed to power other paper components within Vuetify. It is meant to be used as a low level component."
        },
        {
          name: "v-snackbar",

          link: "https://next.vuetifyjs.com/zh-Hans/components/snackbars",
          content:
            "组件用于向用户显示快速消息，Snackbars 支持定位、消失延迟和回调。"
        },
        {
          name: "v-sparkline",

          link:
            "https://next.vuetifyjs.com/zh-Hans/components/sparklines https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute",
          content:
            "The sparkline component can be used to create simple graphs, like GitHub's contribution chart.Any SVG attribute may be used in addition to the ones listed below."
        },
        {
          name: "v-stepper",

          link: "https://next.vuetifyjs.com/zh-Hans/components/steppers",
          content: "组件用于显示步骤进度。"
        },
        {
          name: "v-subheader",

          link: "https://next.vuetifyjs.com/zh-Hans/components/subheaders",
          content: "组件由于分隔列表的各部分。"
        },
        {
          name: "v-tabs",

          link: "https://next.vuetifyjs.com/zh-Hans/components/tabs",
          content:
            "组件用于隐藏可选项目后面的内容。这也可以用作页面的伪导航（pseudo-navigation），其中标签是链接，选项卡子项是内容。"
        },
        {
          name: "v-timeline",

          link: "https://next.vuetifyjs.com/zh-Hans/components/timelines",
          content:
            " <时间线> The v-timeline is useful for stylistically displaying chronological information."
        },
        {
          name: "v-toolbar",

          link: "https://next.vuetifyjs.com/zh-Hans/components/toolbars",
          content:
            " <工具栏> 组件对于任何GUI都很重要，因为它通常是网站导航的主要来源。工具栏组件可以与导航抽屉一起很好地工作，用于隐藏链接并呈现激活器以在移动设备上打开侧边栏。"
        },
        {
          name: "v-tooltip",

          link: "https://next.vuetifyjs.com/zh-Hans/components/tooltips",
          content:
            " <提示> 对于用户悬停在元素上时传递信息很有用。您也可以通过一个v-model以编程方式控制提示组件的显示。"
        },
        {
          name: "v-treeview",

          link: "https://next.vuetifyjs.com/zh-Hans/components/treeview",
          content:
            "<树状结构> The v-treeview component is useful for displaying large amounts of nested data."
        },
        {name:"<v-flex xs12 sm6 offset-sm3>",
        link:"https://next.vuetifyjs.com/zh-Hans/components/cards",
        content:"offest-sm3,空出三个格子"}
      ]
    };
  }
};
</script>


