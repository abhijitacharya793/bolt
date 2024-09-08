import React from "react";

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
  Switch,
  Tooltip,
  Button,
  TabsBody,
  TabPanel,
  Chip,
} from "@material-tailwind/react";
import {
  HomeIcon,
  ChatBubbleLeftEllipsisIcon,
  Cog6ToothIcon,
  PencilIcon,
  FolderArrowDownIcon,
  ArrowDownTrayIcon,
  CommandLineIcon,
  LinkIcon,
  QueueListIcon,
  EyeSlashIcon,
} from "@heroicons/react/24/solid";

export default function Secrets() {
  const authorsTableData = [
    {
      img: "/img/team-2.jpeg",
      name: "John Michael",
      email: "john@creative-tim.com",
      job: ["Manager", "Organization"],
      online: true,
      date: "23/04/18",
    },
    {
      img: "/img/team-1.jpeg",
      name: "Alexa Liras",
      email: "alexa@creative-tim.com",
      job: ["Programator", "Developer"],
      online: false,
      date: "11/01/19",
    },
    {
      img: "/img/team-4.jpeg",
      name: "Laurent Perrier",
      email: "laurent@creative-tim.com",
      job: ["Executive", "Projects"],
      online: true,
      date: "19/09/17",
    },
    {
      img: "/img/team-3.jpeg",
      name: "Michael Levi",
      email: "michael@creative-tim.com",
      job: ["Programator", "Developer"],
      online: true,
      date: "24/12/08",
    },
    {
      img: "/img/bruce-mars.jpeg",
      name: "Bruce Mars",
      email: "bruce@creative-tim.com",
      job: ["Manager", "Executive"],
      online: false,
      date: "04/10/21",
    },
    {
      img: "/img/team-2.jpeg",
      name: "Alexander",
      email: "alexander@creative-tim.com",
      job: ["Programator", "Developer"],
      online: false,
      date: "14/09/20",
    },
  ];
  return (
    <>
      <div className="relative mt-8 h-20 w-full overflow-hidden rounded-xl bg-cover bg-center">
        <div className="absolute inset-0 h-full w-full bg-yellow-100" />
      </div>

      <Card className="mx-3 -mt-16 mb-6 lg:mx-4 border border-blue-gray-100">
        <CardBody className="p-4">
          <div className="mb-10 flex items-center justify-between flex-wrap gap-6">
            <div className="flex items-center gap-6">
              <div className="rounded-lg blue border border-blue-gray-900 w-20 h-20 justify-center items-center flex">
                <EyeSlashIcon fill="blue-gray" className="w-8 h-8" />
              </div>
              <div>
                <Typography
                  variant="h6"
                  color="blue-gray"
                  className="mb-1 uppercase"
                >
                  Secrets
                </Typography>
                <Typography
                  variant="small"
                  className="font-normal text-blue-gray-600"
                >
                  Secrets leaked
                </Typography>
              </div>
            </div>
            <div className="w-96">
              <Tabs value="app">
                <TabsHeader>
                  <Tab value="app">
                    <HomeIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                    App
                  </Tab>
                  <Tab value="message">
                    <ChatBubbleLeftEllipsisIcon className="-mt-0.5 mr-2 inline-block h-5 w-5" />
                    Message
                  </Tab>
                  <Tab value="settings">
                    <Cog6ToothIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                    Settings
                  </Tab>
                </TabsHeader>
              </Tabs>
            </div>
          </div>
          <div className="gird-cols-1 mb-12 grid gap-12 px-4">
            <Card>
              <CardHeader variant="gradient" color="gray" className="mb-8 p-6">
                <Typography variant="h6" color="white">
                  managed by <code className="text-yellow-100">odin</code>
                </Typography>
              </CardHeader>
              <CardBody className="overflow-x-scroll px-0 pt-0 pb-2">
                <table className="w-full min-w-[640px] table-auto">
                  <thead>
                    <tr>
                      {["author", "function", "status", "employed", ""].map(
                        (el) => (
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
                        )
                      )}
                    </tr>
                  </thead>
                  <tbody>
                    {authorsTableData.map(
                      ({ img, name, email, job, online, date }, key) => {
                        const className = `py-3 px-5 ${
                          key === authorsTableData.length - 1
                            ? ""
                            : "border-b border-blue-gray-50"
                        }`;

                        return (
                          <tr key={name}>
                            <td className={className}>
                              <div className="flex items-center gap-4">
                                <Avatar
                                  src={img}
                                  alt={name}
                                  size="sm"
                                  variant="rounded"
                                />
                                <div>
                                  <Typography
                                    variant="small"
                                    color="blue-gray"
                                    className="font-semibold"
                                  >
                                    {name}
                                  </Typography>
                                  <Typography className="text-xs font-normal text-blue-gray-500">
                                    {email}
                                  </Typography>
                                </div>
                              </div>
                            </td>
                            <td className={className}>
                              <Typography className="text-xs font-semibold text-blue-gray-600">
                                {job[0]}
                              </Typography>
                              <Typography className="text-xs font-normal text-blue-gray-500">
                                {job[1]}
                              </Typography>
                            </td>
                            <td className={className}>
                              <Chip
                                variant="gradient"
                                color={online ? "green" : "blue-gray"}
                                value={online ? "online" : "offline"}
                                className="py-0.5 px-2 text-[11px] font-medium w-fit"
                              />
                            </td>
                            <td className={className}>
                              <Typography className="text-xs font-semibold text-blue-gray-600">
                                {date}
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
  );
}
