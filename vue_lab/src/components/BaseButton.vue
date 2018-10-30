<template>
<div>

<div>
    <button class='btn' data-complete-text='finished!' >{{msg}}</button>
</div>
</div>
</template>

<script>
export default {
  name: 'BaseButton',
  data () {
    return {
      msg: 'button'
    }
  }
}
</script>
