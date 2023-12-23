import React from 'react'

export default function ScanOverview() {
    return (
        <>
            <div className="card mt-6">
                <div className="card-header flex flex-row justify-between">
                    <h1 className="h6">Scan Overview</h1>
                    <div className="flex flex-row justify-center items-center">
                        <a href="">
                            <i className="fad fa-chevron-double-down mr-6"></i>
                        </a>
                        <a href="">
                            <i className="fad fa-ellipsis-v"></i>
                        </a>
                    </div>
                </div>
                <div className="card-body grid grid-cols-2 gap-6 lg:grid-cols-1">

                    <div className="p-8">
                        <h1 className="h2">5,337</h1>
                        <p className="text-black font-medium">Scans this month</p>

                        <div className="mt-20 mb-2 flex items-center">
                            <div className="py-1 px-3 rounded bg-green-200 text-green-900 mr-3">
                                <i className="fa fa-caret-up"></i>
                            </div>
                            <p className="text-black"><span className="num-2 text-green-400"></span><span className="text-green-400">% more scan</span> in comparison to last month.</p>
                        </div>

                        <div className="flex items-center">
                            <div className="py-1 px-3 rounded bg-red-200 text-red-900 mr-3">
                                <i className="fa fa-caret-down"></i>
                            </div>
                            <p className="text-black"><span className="num-2 text-red-400"></span><span className="text-red-400">% revenue per sale</span> in comparison to last month.</p>
                        </div>

                        <a href="#" className="btn-shadow mt-6">view details</a>

                    </div>

                    <div className="">
                        <div id="sealsOverview"></div>
                    </div>
                </div>
            </div>
        </>
    )
}
