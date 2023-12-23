import React from 'react'
import {
    Timeline,
    TimelineItem,
    TimelineConnector,
    TimelineHeader,
    TimelineIcon,
    TimelineBody,
    Typography,
} from "@material-tailwind/react";

export default function ScanTimeline() {
    return (
        <>
            <div className="">
                <Timeline>
                    <TimelineItem>
                        <TimelineConnector />
                        <TimelineHeader className="h-3">
                            <TimelineIcon />
                            <Typography variant="h6" color="blue-gray" className="leading-none">
                                Scan created
                            </Typography>
                        </TimelineHeader>
                        <TimelineBody className="pb-8">
                            <Typography variant="small" color="gary" className="font-normal text-gray-600">
                                <p>Count of APIs:  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;120</p>
                                <p>Number of GET APIs: &emsp;&emsp;&emsp;100</p>
                                <p>Number of POST APIs: &emsp;20</p>
                            </Typography>
                        </TimelineBody>
                    </TimelineItem>
                    <TimelineItem>
                        <TimelineConnector />
                        <TimelineHeader className="h-3">
                            <TimelineIcon />
                            <Typography variant="h6" color="blue-gray" className="leading-none">
                                Scan started
                            </Typography>
                        </TimelineHeader>
                        <TimelineBody className="pb-8">
                            <Typography variant="small" color="gary" className="font-normal text-gray-600">
                                The key to more success is to have a lot of pillows. Put it this way, it took me
                                twenty five years to get these plants, twenty five years of blood sweat and tears, and
                                I&apos;m never giving up, I&apos;m just getting started. I&apos;m up to something. Fan
                                luv.
                            </Typography>
                        </TimelineBody>
                    </TimelineItem>
                    <TimelineItem>
                        <TimelineHeader className="h-3">
                            <TimelineIcon />
                            <Typography variant="h6" color="blue-gray" className="leading-none">
                                Scan Completed
                            </Typography>
                        </TimelineHeader>
                        <TimelineBody>
                            <Typography variant="small" color="gary" className="font-normal text-gray-600">
                                The key to more success is to have a lot of pillows. Put it this way, it took me
                                twenty five years to get these plants, twenty five years of blood sweat and tears, and
                                I&apos;m never giving up, I&apos;m just getting started. I&apos;m up to something. Fan
                                luv.
                            </Typography>
                        </TimelineBody>
                    </TimelineItem>
                </Timeline>
            </div>
        </>
    )
}
