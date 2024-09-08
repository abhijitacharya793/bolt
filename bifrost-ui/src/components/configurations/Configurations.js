import React from 'react'
import { useParams } from 'react-router';

import {
    Card,
    CardBody,
    CardHeader,
    Typography,
    Switch,
} from "@material-tailwind/react";
import {
    Cog6ToothIcon,
    QueueListIcon,
} from "@heroicons/react/24/solid";

export default function ScanDetails() {
    const params = useParams();
    const platformSettingsData = [
        {
            title: "account",
            options: [
                {
                    checked: true,
                    label: "Email me when someone follows me",
                },
                {
                    checked: false,
                    label: "Email me when someone answers on my post",
                },
                {
                    checked: true,
                    label: "Email me when someone mentions me",
                },
            ],
        },
        {
            title: "application",
            options: [
                {
                    checked: false,
                    label: "New launches and projects",
                },
                {
                    checked: true,
                    label: "Monthly product updates",
                },
                {
                    checked: false,
                    label: "Subscribe to newsletter",
                },
            ],
        },
    ];

    return (
        <>
            <div className="relative mt-8 h-20 w-full overflow-hidden rounded-xl bg-cover bg-center">
                <div className="absolute inset-0 h-full w-full bg-green-100" />
            </div>

            <Card className="mx-3 -mt-16 mb-6 lg:mx-4 border border-blue-gray-100">
                <CardBody className="p-4">
                    <div className="mb-10 flex items-center justify-between flex-wrap gap-6">
                        <div className="flex items-center gap-6">
                            <div className="rounded-lg blue border border-blue-gray-900 w-20 h-20 justify-center items-center flex">
                                <Cog6ToothIcon fill="blue-gray" className="w-8 h-8" />
                            </div>
                            <div>
                                <Typography variant="h5" color="blue-gray" className="mb-1">
                                    Configurations
                                </Typography>
                                <Typography
                                    variant="small"
                                    className="font-normal text-blue-gray-600"
                                >
                                    Configure Platform and User level configs
                                </Typography>
                            </div>
                        </div>
                    </div>
                    <div className="gird-cols-1 mb-12 grid gap-12 px-4">
                        <Card>
                            <CardHeader variant="gradient" color="gray" className="mb-8 p-6">
                                <Typography variant="h6" color="white">
                                    managed by <code className='text-green-100'>bifrost</code>
                                </Typography>
                            </CardHeader>
                            <CardBody className="px-0 pt-0 pb-2">
                                <div className="grid grid-cols-6 gap-4">
                                    <div className='col-span-4'>
                                        <div className="grid grid-cols-6 gap-4 px-4 py-2">
                                            <div className='col-span-3'>
                                                <div>
                                                    <Typography variant="h6" color="blue-gray" className="mb-3">
                                                        Platform Settings
                                                    </Typography>
                                                    <div className="flex flex-col gap-12">
                                                        {platformSettingsData.map(({ title, options }) => (
                                                            <div key={title}>
                                                                <Typography className="mb-4 block text-xs font-semibold uppercase text-blue-gray-500">
                                                                    {title}
                                                                </Typography>
                                                                <div className="flex flex-col gap-6">
                                                                    {options.map(({ checked, label }) => (
                                                                        <Switch
                                                                            key={`${label}1`}
                                                                            id={`${label}1`}
                                                                            label={label}
                                                                            defaultChecked={checked}
                                                                            labelProps={{
                                                                                className: "text-sm font-normal text-blue-gray-500",
                                                                            }}
                                                                        />
                                                                    ))}
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </div>
                                            </div>
                                            <div className='col-span-3'>
                                                <div>
                                                    <Typography variant="h6" color="blue-gray" className="mb-3">
                                                        Platform Settings
                                                    </Typography>
                                                    <div className="flex flex-col gap-12">
                                                        {platformSettingsData.map(({ title, options }) => (
                                                            <div key={title}>
                                                                <Typography className="mb-4 block text-xs font-semibold uppercase text-blue-gray-500">
                                                                    {title}
                                                                </Typography>
                                                                <div className="flex flex-col gap-6">
                                                                    {options.map(({ checked, label }) => (
                                                                        <Switch
                                                                            key={`${label}2`}
                                                                            id={`${label}2`}
                                                                            label={label}
                                                                            defaultChecked={checked}
                                                                            labelProps={{
                                                                                className: "text-sm font-normal text-blue-gray-500",
                                                                            }}
                                                                        />
                                                                    ))}
                                                                </div>
                                                            </div>
                                                        ))}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div className='col-span-2 p-4'>
                                        {/* <ScanTimeline /> */}
                                    </div>
                                </div>
                            </CardBody>
                        </Card>
                    </div>
                </CardBody>
            </Card>
        </>
    )
}
