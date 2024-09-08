import React from "react";
import {
  Timeline,
  TimelineItem,
  TimelineConnector,
  TimelineHeader,
  TimelineIcon,
  TimelineBody,
  Typography,
} from "@material-tailwind/react";

export default function ScanTimeline({ scanDetails }) {
  console.log(scanDetails);
  return (
    <>
      <div className="mt-16">
        <Timeline>
          <TimelineItem>
            <TimelineConnector />
            <TimelineHeader className="h-3">
              <TimelineIcon />
              <Typography
                variant="h6"
                color="blue-gray"
                className="leading-none"
              >
                Scan created
              </Typography>
            </TimelineHeader>
            <TimelineBody className="pb-8">
              <Typography
                variant="small"
                color="gary"
                className="font-normal text-gray-600"
              >
                <table className="w-80 table-auto text-left border-2 shadow-md">
                  <tbody>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4 border-b border-blue-gray-50">
                        Count of APIs
                      </td>
                      <td className="p-4 border-b border-blue-gray-50">
                        {scanDetails.length}
                      </td>
                    </tr>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4 border-b border-blue-gray-50">
                        Number of GET APIs
                      </td>
                      <td className="p-4 border-b border-blue-gray-50">120</td>
                    </tr>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4">Number of POST APIs</td>
                      <td className="p-4">120</td>
                    </tr>
                  </tbody>
                </table>
              </Typography>
            </TimelineBody>
          </TimelineItem>
          <TimelineItem>
            <TimelineConnector />
            <TimelineHeader className="h-3">
              <TimelineIcon />
              <Typography
                variant="h6"
                color="blue-gray"
                className="leading-none"
              >
                Scan started
              </Typography>
            </TimelineHeader>
            <TimelineBody className="pb-8">
              <Typography
                variant="small"
                color="gary"
                className="font-normal text-gray-600"
              >
                <table className="w-80 table-auto text-left border-2 shadow-md">
                  <tbody>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4 border-b border-blue-gray-50">
                        Attack Power
                      </td>
                      <td className="p-4 border-b border-blue-gray-50">High</td>
                    </tr>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4 border-b border-blue-gray-50">
                        Rate Limit
                      </td>
                      <td className="p-4 border-b border-blue-gray-50">5</td>
                    </tr>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4">Application Type</td>
                      <td className="p-4">Web</td>
                    </tr>
                  </tbody>
                </table>
              </Typography>
            </TimelineBody>
          </TimelineItem>
          <TimelineItem>
            <TimelineHeader className="h-3">
              <TimelineIcon />
              <Typography
                variant="h6"
                color="blue-gray"
                className="leading-none"
              >
                Scan Completed
              </Typography>
            </TimelineHeader>
            <TimelineBody>
              <Typography
                variant="small"
                color="gary"
                className="font-normal text-gray-600"
              >
                <table className="w-80 table-auto text-left border-2 shadow-md">
                  <tbody>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4 border-b border-blue-gray-50">
                        Risk Score
                      </td>
                      <td className="p-4 border-b border-blue-gray-50">120</td>
                    </tr>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4 border-b border-blue-gray-50">
                        Number of Vulnerabilities Identified
                      </td>
                      <td className="p-4 border-b border-blue-gray-50">120</td>
                    </tr>
                    <tr className="even:bg-blue-gray-50/50">
                      <td className="p-4">Number of Secrets Identified</td>
                      <td className="p-4">120</td>
                    </tr>
                  </tbody>
                </table>
              </Typography>
            </TimelineBody>
          </TimelineItem>
        </Timeline>
      </div>
    </>
  );
}
