<template>
  <div class="common-layout">
    <el-container>
      <el-header> 'head' </el-header>
      <el-container>
        <el-main>
          <BodyLayouts></BodyLayouts>
        </el-main>
      </el-container>
      <el-footer> 'foot' </el-footer>
    </el-container>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { BodyLayouts } from './index'
export default defineComponent({
  components: { BodyLayouts },
})
</script>
