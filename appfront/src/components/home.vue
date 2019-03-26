<template>
  <div>
    <el-steps :active="active" finish-status="success">
      <el-step title="步骤 1" description="选择需要配置的终端">
        <el-row>
          <el-button type="primary">主要按钮</el-button>
        </el-row>
      </el-step>
      <el-step title="步骤 2" description="ID校验"></el-step>
      <el-step title="步骤 3" description="取流设置"></el-step>
      <el-step title="步骤 3" description="算法配置"></el-step>
    </el-steps>

    <el-button style="margin-top: 12px;" @click="next">下一步</el-button>
  </div>
</template>

<script>
  export default {
    name: "home",
    data() {
      return {
        active: 0
      }
    },
    methods: {
      next() {
        if (this.active++ > 3) this.active = 0;
      }
    }
  }
</script>

<style scoped>

</style>
