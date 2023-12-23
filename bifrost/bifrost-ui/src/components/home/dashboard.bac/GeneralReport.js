import React from 'react'

export default function GeneralReport() {
    return (
        <>
            <div className="grid grid-cols-5 gap-6 xl:grid-cols-1">
                <div className="report-card">
                    <div className="card">
                        <div className="card-body flex flex-col">

                            <div className="flex flex-row justify-between items-center">
                                <div className="h6 text-indigo-700 fad fa-bolt"></div>
                                <span className="rounded-full text-white badge bg-teal-400 text-xs">
                                    12%
                                    <i className="fal fa-chevron-up ml-1"></i>
                                </span>
                            </div>
                            <div className="mt-8">
                                <h1 className="h5">1293</h1>
                                <p>total apis</p>
                            </div>

                        </div>
                    </div>
                    <div className="footer bg-white p-1 mx-4 border border-t-0 rounded rounded-t-none"></div>
                </div>
                <div className="report-card">
                    <div className="card">
                        <div className="card-body flex flex-col">

                            <div className="flex flex-row justify-between items-center">
                                <div className="h6 text-red-700 fad fa-chevron-double-up"></div>
                                <span className="rounded-full text-white badge bg-red-400 text-xs">
                                    6%
                                    <i className="fal fa-chevron-down ml-1"></i>
                                </span>
                            </div>
                            <div className="mt-8">
                                <h1 className="h5">20</h1>
                                <p>critical</p>
                            </div>

                        </div>
                    </div>
                    <div className="footer bg-white p-1 mx-4 border border-t-0 rounded rounded-t-none"></div>
                </div>
                <div className="report-card">
                    <div className="card">
                        <div className="card-body flex flex-col">

                            <div className="flex flex-row justify-between items-center">
                                <div className="h6 text-yellow-600 fad fa-chevron-up"></div>
                                <span className="rounded-full text-white badge bg-red-400 text-xs">
                                    72%
                                    <i className="fal fa-chevron-up ml-1"></i>
                                </span>
                            </div>
                            <div className="mt-8">
                                <h1 className="h5">113</h1>
                                <p>high</p>
                            </div>

                        </div>
                    </div>
                    <div className="footer bg-white p-1 mx-4 border border-t-0 rounded rounded-t-none"></div>
                </div>
                <div className="report-card">
                    <div className="card">
                        <div className="card-body flex flex-col">

                            <div className="flex flex-row justify-between items-center">
                                <div className="h6 text-green-700 fad fa-chevron-down"></div>
                                <span className="rounded-full text-white badge bg-teal-400 text-xs">
                                    150%
                                    <i className="fal fa-chevron-up ml-1"></i>
                                </span>
                            </div>
                            <div className="mt-8">
                                <h1 className="h5">150</h1>
                                <p>medium</p>
                            </div>

                        </div>
                    </div>
                    <div className="footer bg-white p-1 mx-4 border border-t-0 rounded rounded-t-none"></div>
                </div>
                <div className="report-card">
                    <div className="card">
                        <div className="card-body flex flex-col">

                            <div className="flex flex-row justify-between items-center">
                                <div className="h6 text-green-700 fad fa-chevron-double-down"></div>
                                <span className="rounded-full text-white badge bg-teal-400 text-xs">
                                    150%
                                    <i className="fal fa-chevron-up ml-1"></i>
                                </span>
                            </div>
                            <div className="mt-8">
                                <h1 className="h5">10</h1>
                                <p>low</p>
                            </div>

                        </div>
                    </div>
                    <div className="footer bg-white p-1 mx-4 border border-t-0 rounded rounded-t-none"></div>
                </div>

            </div>
        </>
    )
}
