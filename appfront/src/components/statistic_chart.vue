<template>
  <div>
    <el-container style="height: 100vh; border: 1px solid #eee">
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu :default-openeds="['1','2', '3']" router>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-message"></i>终端配置</template>
            <el-menu-item-group>
              <template slot="title"></template>
              <el-menu-item index="/map">终端地图</el-menu-item>
              <el-menu-item index="/home">算法配置</el-menu-item>
            </el-menu-item-group>
            <el-menu-item index="1-3">删除终端</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-menu"></i>数据管理</template>
            <el-menu-item index="2-1">报警信息</el-menu-item>
            <el-menu-item index="/statistic_chart">统计图表</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-setting"></i>视频查看</template>
            <el-menu-item-group>
              <template slot="title"></template>
              <el-menu-item index="3-1">实时浏览</el-menu-item>
              <el-menu-item index="3-2">警报视频</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>查看</el-dropdown-item>
              <el-dropdown-item>新增</el-dropdown-item>
              <el-dropdown-item>删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <span>admin</span>
        </el-header>

        <el-main>
          <div class="card">
            <el-row>
              <el-col :span="5">
                <el-card shadow="hover">
                  帽子报警
                </el-card>
              </el-col>

              <el-col :span="5" style="margin-left: 30px; margin-right: 30px">
                <el-card shadow="hover">
                  老鼠报警
                </el-card>
              </el-col>

              <el-col :span="5">
                <el-card shadow="hover">
                  口罩报警
                </el-card>
              </el-col>
            </el-row>
          </div>
          <div id="myChart" :style="{width: '100%',height: '100%'}"></div>
        </el-main>

        <el-footer style="text-align: center; font-size: 10px">
          版权所有 © 上海大学
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "statistic_chart",
    mounted() {
      this.drawLine();
    },
    data() {
      return {};
    },
    methods: {
      drawLine() {
        // 基于准备好的dom，初始化echarts实例
        let myChart = this.$echarts.init(document.getElementById('myChart'))
        // 绘制图表
        myChart.setOption({
          title: {
            text: '堆叠区域图'
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              label: {
                backgroundColor: '#6a7985'
              }
            }
          },
          legend: {
            data: ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎']
          },
          toolbox: {
            feature: {
              saveAsImage: {}
            }
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: [
            {
              type: 'category',
              boundaryGap: false,
              data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
            }
          ],
          yAxis: [
            {
              type: 'value'
            }
          ],
          series: [
            {
              name: '邮件营销',
              type: 'line',
              stack: '总量',
              areaStyle: {},
              data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
              name: '联盟广告',
              type: 'line',
              stack: '总量',
              areaStyle: {},
              data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
              name: '视频广告',
              type: 'line',
              stack: '总量',
              areaStyle: {},
              data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
              name: '直接访问',
              type: 'line',
              stack: '总量',
              areaStyle: {normal: {}},
              data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
              name: '搜索引擎',
              type: 'line',
              stack: '总量',
              label: {
                normal: {
                  show: true,
                  position: 'top'
                }
              },
              areaStyle: {normal: {}},
              data: [820, 932, 901, 934, 1290, 1330, 1320]
            }
          ]
        });
      }

    }
  }
</script>

<style scoped>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

  .el-aside {
    color: #333;
  }

  .card {
    text-align: center;
    width: 1500px;
    margin-left: 250px;
    margin-bottom: 30px;
    margin-top: 30px;
  }
</style>
