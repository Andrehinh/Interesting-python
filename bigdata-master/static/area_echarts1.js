$(function(){
        $.ajax({
            url: '/get_map_data',
            type: 'get',
            dataTpye: 'json',
            success: function (res) {
                mymap(res)
            }
        });
        function mymap(data) {
            var worldMapContainer1 = document.getElementById('map_1');
            var myChart = echarts.init(worldMapContainer1);
            var option = {
                tooltip: {
                    trigger: 'item'
                },
                visualMap: {
                    min: 0,
                    max: 1500,
                    show: false,
                    left: 'right',
                    top: 'bottom',
                    text: ['高', '低'], // 文本，默认为数值文本
                    calculable: true,
                    //		color: ['#26cfe4', '#f2b600', '#ec5845'],
                    textStyle: {
                        color: '#fff'
                    }
                },
                series: [{
                        name: '确诊人数',
                        type: 'map',
                        aspectScale: 0.75,
                        zoom: 1.2,
                        mapType: 'china',
                        roam: false,
                        label: {
                            show: true,
                            normal: {
                                show: true,//显示省份标签
                                textStyle:{color:"#c71585"}//省份标签字体颜色
                            },
                            emphasis: {//对应的鼠标悬浮效果
                                show: false,
                                textStyle:{color:"#800080"}
                            }
                        },
                        itemStyle: {
                            normal: {
                                borderWidth: .5,//区域边框宽度
                                borderColor: '#002097',//区域边框颜色
                                areaColor:"#4c60ff",//区域颜色
                            },
                            emphasis: {
                                borderWidth: .5,
                                borderColor: '#4b0082',
                                areaColor:"#ffdead",
                            }
                        },
                        data: data
                        // data: [{'name': '湖北', 'value': 300}, {'name': '辽宁', 'value': 120}, {'name': '新疆', 'value': 13},
                        //     {'name': '重启', 'value': 14}]

                    }
                ]
            };
            myChart.setOption(option);

            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            myChart.on('click', function (params) {//点击事件
                if (params.componentType === 'series') {
                }
            })
            }

	}
)