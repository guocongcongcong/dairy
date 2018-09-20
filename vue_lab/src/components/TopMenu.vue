<template>
    <section>
        <div>
            <a id = "logo" href="/"></a>
            <ul id="nav"></ul>
            <div id='app'>
                {{message}}
            </div>
        </div>
    </section>
</template>
<script>
export default {
    el:"#app",
    date:{
        message:'Hello Vue'
    }
}
</script>
<style>

</style>
