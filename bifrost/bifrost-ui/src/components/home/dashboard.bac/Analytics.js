import React from 'react'
import Chart from "react-apexcharts";


import happy from '../../../static/img/happy.svg'

export default function Analytics() {
    // var chart = new ApexCharts(analytics_1[0], options("area", '51px', numArr(10, 99), '#4fd1c5'));
    // var chart_1 = new ApexCharts(analytics_1[1], options("area", '51px', numArr(10, 99), '#4c51bf'));
    // chart.render();
    // chart_1.render();
    var numArr = function (length, max) {
        return Array.from({ length: length }, () => Math.floor(Math.random() * max));
    }
    var chart1 = {
        options: {
            chart: {
                sparkline: {
                    enabled: true
                },
            },
            stroke: {
                curve: 'smooth',
                colors: ["#4fd1c5"]
            },
            fill: {
                colors: ['#4fd1c5']
            },
        },
        series: [
            {
                name: "series-1",
                data: numArr(10, 99)
            }
        ]
    };
    var chart2 = {
        options: {
            chart: {
                sparkline: {
                    enabled: true
                },
            },
            stroke: {
                curve: 'smooth',
                colors: ["#4c51bf"]
            },
            fill: {
                colors: ['#4c51bf']
            },
        },
        series: [
            {
                name: "series-1",
                data: numArr(10, 99)
            }
        ]
    };


    return (
        <>
            <div className="mt-6 grid grid-cols-2 gap-6 xl:grid-cols-1">
                <div className="card bg-teal-400 border-teal-400 shadow-md text-white">
                    <div className="card-body flex flex-row">
                        <div className="img-wrapper w-40 h-40 flex justify-center items-center">
                            <img src={happy} alt="img title" />
                        </div>
                        <div className="py-2 ml-10">
                            <h1 className="h6">Congratulations, Abhi!</h1>
                            <p className="text-white text-xs">We've finished all of your tasks for this week.</p>

                            <ul className="mt-4">
                                <li className="text-sm font-light"><i className="fad fa-check-double mr-2 mb-2"></i> Yahoo API</li>
                                <li className="text-sm font-light"><i className="fad fa-check-double mr-2 mb-2"></i> Lessonly Bugbounty</li>
                                <li className="text-sm font-light"><i className="fad fa-check-double mr-2"></i> Flipkart Mobile</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="flex flex-col">
                    <div className="alert alert-dark mb-6">
                        Your mission, should you choose to accept it...
                        {/* <a className="ml-2" target="_blank" href="https://twitter.com/abhijit_a793">@abhijit_a793</a> */}
                    </div>
                    <div className="grid grid-cols-2 gap-6 h-full">
                        <div className="card">
                            <div className="py-3 px-4 flex flex-row justify-between">
                                <h1 className="h6">
                                    <span className="">113</span>k
                                    <p>page view</p>
                                </h1>

                                <div className="bg-teal-200 text-teal-700 border-teal-300 border w-10 h-10 rounded-full flex justify-center items-center">
                                    <i className="fad fa-eye"></i>
                                </div>
                            </div>
                            <div className="pb-0">
                                <Chart
                                    options={chart1.options}
                                    series={chart1.series}
                                    type="area"
                                    height={57}
                                />
                            </div>
                        </div>

                        <div className="card">
                            <div className="py-3 px-4 flex flex-row justify-between">
                                <h1 className="h6">
                                    <span className="">356</span>k
                                    <p>Unique Users</p>
                                </h1>

                                <div className="bg-indigo-200 text-indigo-700 border-indigo-300 border w-10 h-10 rounded-full flex justify-center items-center">
                                    <i className="fad fa-users-crown"></i>
                                </div>
                            </div>
                            <div>
                                <Chart
                                    options={chart2.options}
                                    series={chart2.series}
                                    type="area"
                                    height={57}
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
