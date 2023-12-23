import React from 'react'

import {
    Card,
    CardBody,
    CardHeader,
    CardFooter,
    Avatar,
    Typography,
    Tabs,
    TabsHeader,
    Tab,
    Chip,
} from "@material-tailwind/react";
import {
    ExclamationTriangleIcon,
    ExclamationCircleIcon,
    ShieldExclamationIcon,
    NoSymbolIcon,
} from "@heroicons/react/24/solid";

export default function Vulnerabilities() {
    const vulnerabilities = [
        {
            vulnerability: "Error based SQL Injection",
            risk: "SQL Injection",
            abbreviation: "SQLi",
            severity: "critical",
            cvss: "9.0",
        },
        {
            vulnerability: "Reflected Cross Site Scripting",
            risk: "Cross Site Scripting",
            abbreviation: "XSS",
            severity: "high",
            cvss: "7.5",
        }
    ];
    return (
        <>
            <div className="relative mt-8 h-36 w-full overflow-hidden rounded-xl bg-cover bg-center">
                <div className="absolute inset-0 h-full w-full bg-indigo-100" />
            </div>

            <Card className="mx-3 -mt-16 mb-6 lg:mx-4 border border-blue-gray-100">
                <CardBody className="p-4">
                    <div className="mb-10 flex items-center justify-between flex-wrap gap-6">
                        <div className="flex items-center gap-6">
                            <div className="rounded-lg blue border border-blue-gray-900 w-20 h-20 justify-center items-center flex">
                                <ExclamationTriangleIcon fill="blue-gray" className="w-8 h-8" />
                            </div>
                            <div>
                                <Typography variant="h5" color="blue-gray" className="mb-1">
                                    Vulnerabilities
                                </Typography>
                                <Typography
                                    variant="small"
                                    className="font-normal text-blue-gray-600"
                                >
                                    Get a list of all
                                </Typography>
                            </div>
                        </div>
                        <div className="w-full">
                            <Tabs value="app">
                                <TabsHeader>
                                    <Tab value="all">
                                        <ExclamationCircleIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                                        All
                                    </Tab>
                                    <Tab value="critical">
                                        <ExclamationCircleIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                                        Critical
                                    </Tab>
                                    <Tab value="high">
                                        <ExclamationTriangleIcon className="-mt-0.5 mr-2 inline-block h-5 w-5" />
                                        High
                                    </Tab>
                                    <Tab value="medium">
                                        <ShieldExclamationIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                                        Medium
                                    </Tab>
                                    <Tab value="low">
                                        <NoSymbolIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                                        Low
                                    </Tab>
                                </TabsHeader>
                            </Tabs>
                        </div>
                    </div>
                    <div className="gird-cols-1 mb-12 grid gap-12 px-4">
                        <Card>
                            <CardHeader variant="gradient" color="gray" className="mb-8 p-6">
                                <Typography variant="h6" color="white">
                                    managed by <code className='text-indigo-100'>thor</code>
                                </Typography>
                            </CardHeader>
                            <CardBody className="overflow-x-scroll px-0 pt-0 pb-2">
                                <table className="w-full min-w-[640px] table-auto">
                                    <thead>
                                        <tr>
                                            {["vulnerability", "risk", "severity", "cvss rating", ""].map((el) => (
                                                <th
                                                    key={el}
                                                    className="border-b border-blue-gray-50 py-3 px-5 text-left"
                                                >
                                                    <Typography
                                                        variant="small"
                                                        className="text-[11px] font-bold uppercase text-blue-gray-400"
                                                    >
                                                        {el}
                                                    </Typography>
                                                </th>
                                            ))}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {vulnerabilities.map(
                                            ({ vulnerability, risk, abbreviation, severity, cvss }, key) => {
                                                const className = `py-3 px-5 ${key === vulnerabilities.length - 1
                                                    ? ""
                                                    : "border-b border-blue-gray-50"
                                                    }`;

                                                return (
                                                    <tr key={vulnerability}>
                                                        <td className={className}>
                                                            <div className="flex items-center gap-4">
                                                                <ExclamationCircleIcon className='h-8 w-8 text-red-300' />
                                                                <div>
                                                                    <Typography
                                                                        variant="small"
                                                                        color="blue-gray"
                                                                        className="font-semibold"
                                                                    >
                                                                        {vulnerability}
                                                                    </Typography>
                                                                    <Typography className="text-xs font-normal text-blue-gray-500">
                                                                        {risk}
                                                                    </Typography>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td className={className}>
                                                            <Typography className="text-xs font-semibold text-blue-gray-600">
                                                                {abbreviation}
                                                            </Typography>
                                                        </td>
                                                        <td className={className}>
                                                            <Chip
                                                                variant="gradient"
                                                                color={severity === "critical" ? "red" : "orange"}
                                                                value={severity}
                                                                className="py-0.5 px-2 text-[11px] font-medium w-fit"
                                                            />
                                                        </td>
                                                        <td className={className}>
                                                            <Typography className="text-xs font-semibold text-blue-gray-600">
                                                                {cvss}
                                                            </Typography>
                                                        </td>
                                                        <td className={className}>
                                                            <Typography
                                                                as="a"
                                                                href="#"
                                                                className="text-xs font-semibold text-blue-gray-600"
                                                            >
                                                                Edit
                                                            </Typography>
                                                        </td>
                                                    </tr>
                                                );
                                            }
                                        )}
                                    </tbody>
                                </table>
                            </CardBody>
                        </Card>
                    </div>
                </CardBody>
            </Card>
        </>
    )
}
