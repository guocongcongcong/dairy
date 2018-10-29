<template>
    <section>
        <div>
            <a id = "logo" href="/"></a>
            <ul id="nav"></ul>
            <div id='app'>
                {{message}}
            </div>
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">吃饭</a></li>
                <li><a href="#">睡觉</a></li>
                <li><a href="#">打勇士</a></li>
            </ul>
            <button class="btn" data-toggle="button" >…</button>
        </div>
    </section>
</template>

<script>
export default {
  date: {
    message: 'Hello Vue'
  }
}
</script>
<style>
</style>
