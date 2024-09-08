import React, { useEffect, useState } from "react";

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
  Button,
} from "@material-tailwind/react";
import {
  ExclamationTriangleIcon,
  ExclamationCircleIcon,
  ShieldExclamationIcon,
  NoSymbolIcon,
  FlagIcon,
} from "@heroicons/react/24/solid";
import { PrismAsyncLight as SyntaxHighlighter } from "react-syntax-highlighter";
import prism from "react-syntax-highlighter/dist/esm/styles/prism/prism";
import { useNavigate } from "react-router-dom";
import no_results from "../../static/img/no_results.jpg";

export default function Vulnerabilities() {
  const [vulnerabilities, setVulnerabilities] = useState([]);
  const [risks, setRisks] = useState([]);
  const [tags, setTags] = useState([]);
  const [results, setResults] = useState([]);

  const [data, setData] = useState([]);

  const getVulnerabilities = () => {
    fetch("http://yggdrasil-api:8337/yggdrasil/v1/vulnerabilitys", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        setVulnerabilities(data);
        console.log(data);
      })
      .catch((err) => console.error(err));
  };
  const getResults = () => {
    fetch("http://hiemdall-api:8338/hiemdall/v1/result", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        setResults(data);
        setData(data);
        console.log(data);
      })
      .catch((err) => console.error(err));
  };
  const getRisks = () => {
    fetch("http://yggdrasil-api:8337/yggdrasil/v1/risks", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => setRisks(data))
      .catch((err) => console.error(err));
  };
  const getTags = () => {
    fetch("http://yggdrasil-api:8337/yggdrasil/v1/tags", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => setTags(data))
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    getVulnerabilities();
    getResults();
    getRisks();
    getTags();
  }, []);

  const handleFilter = (severity) => {
    if (severity === "a") {
      setData(results);
    } else {
      setData(
        results.filter(function (res) {
          return (
            vulnerabilities[res.vulnerability_id - 1].severity === severity
          );
        })
      );
    }
  };

  let navigate = useNavigate();
  const navigateToVulnerabilityDetails = (e) => {
    navigate(`/vulnerabilities/vulnerabilitydetails/${e.target.name}`);
  };

  return (
    <>
      <div className="relative mt-8 h-20 w-full overflow-hidden rounded-xl bg-cover bg-center">
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
                <Typography
                  variant="h6"
                  color="blue-gray"
                  className="mb-1 uppercase"
                >
                  Vulnerabilities
                </Typography>
                <Typography
                  variant="small"
                  className="font-normal text-blue-gray-600"
                >
                  Get a list of all vulnerabilities detected by Bolt
                </Typography>
              </div>
            </div>

            {data.length > 0 && (
              <div className="w-full">
                <Tabs value="all">
                  <TabsHeader>
                    <Tab
                      value="all"
                      onClick={() => {
                        handleFilter("a");
                      }}
                    >
                      <ExclamationCircleIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                      All
                    </Tab>
                    <Tab
                      value="critical"
                      onClick={() => {
                        handleFilter("c");
                      }}
                    >
                      <ExclamationCircleIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                      Critical
                    </Tab>
                    <Tab
                      value="high"
                      onClick={() => {
                        handleFilter("h");
                      }}
                    >
                      <ExclamationTriangleIcon className="-mt-0.5 mr-2 inline-block h-5 w-5" />
                      High
                    </Tab>
                    <Tab
                      value="medium"
                      onClick={() => {
                        handleFilter("m");
                      }}
                    >
                      <ShieldExclamationIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                      Medium
                    </Tab>
                    <Tab
                      value="low"
                      onClick={() => {
                        handleFilter("l");
                      }}
                    >
                      <NoSymbolIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                      Low
                    </Tab>
                    <Tab
                      value="info"
                      onClick={() => {
                        handleFilter("i");
                      }}
                    >
                      <FlagIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                      Info
                    </Tab>
                  </TabsHeader>
                </Tabs>
              </div>
            )}
          </div>
          <div className="gird-cols-1 mb-12 grid gap-12 px-4">
            <Card>
              <CardHeader variant="gradient" color="gray" className="mb-8 p-6">
                <Typography variant="h6" color="white">
                  managed by <code className="text-indigo-100">thor</code>
                </Typography>
              </CardHeader>
              <CardBody className="overflow-x-scroll px-0 pt-0 pb-2">
                {(data.length > 0 && (
                  <table className="w-full min-w-[640px] table-auto">
                    <thead>
                      <tr>
                        {[
                          "scan id",
                          "vulnerability",
                          "severity",
                          "payload string",
                          "link",
                          "",
                        ].map((el) => (
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
                      {data.map(
                        (
                          {
                            id,
                            curl_command,
                            matched_at,
                            payload_str,
                            scan_id,
                            template_id,
                            uuid,
                            vulnerability_id,
                          },
                          key
                        ) => {
                          if (vulnerabilities.length > 0) {
                            const name =
                              vulnerabilities[vulnerability_id - 1]["name"];
                            const power =
                              vulnerabilities[vulnerability_id - 1]["power"];
                            const risk =
                              vulnerabilities[vulnerability_id - 1]["risk"];
                            const severity =
                              vulnerabilities[vulnerability_id - 1]["severity"];
                            const tag =
                              vulnerabilities[vulnerability_id - 1]["tag"];

                            const className = `py-3 px-5 ${
                              key === results.length - 1
                                ? ""
                                : "border-b border-blue-gray-50"
                            }`;

                            return (
                              <tr key={key}>
                                <td className={className}>
                                  <div className="flex items-center gap-4">
                                    {scan_id}
                                  </div>
                                </td>
                                <td className={className}>
                                  <div className="flex items-center gap-4">
                                    <ExclamationCircleIcon
                                      className={`h-8 w-8 ${
                                        severity === "c"
                                          ? "text-red-300"
                                          : severity === "h"
                                          ? "text-orange-300"
                                          : severity === "m"
                                          ? "text-yellow-300"
                                          : severity === "l"
                                          ? "text-green-300"
                                          : "text-gray-900"
                                      } `}
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
                                        {
                                          risks.filter(function (rk) {
                                            return rk.id === risk;
                                          })[0]["name"]
                                        }
                                      </Typography>
                                    </div>
                                  </div>
                                </td>
                                <td className={className}>
                                  <Chip
                                    variant="gradient"
                                    color={
                                      severity === "c"
                                        ? "red"
                                        : severity === "h"
                                        ? "orange"
                                        : severity === "m"
                                        ? "yellow"
                                        : severity === "l"
                                        ? "green"
                                        : "gray"
                                    }
                                    value={
                                      severity === "c"
                                        ? "critical"
                                        : severity === "h"
                                        ? "high"
                                        : severity === "m"
                                        ? "medium"
                                        : severity === "l"
                                        ? "low"
                                        : "info"
                                    }
                                    className="py-0.5 px-2 text-[11px] font-medium w-fit"
                                  />
                                </td>
                                {/*  */}
                                <td className={className}>
                                  <Typography className="text-xs">
                                    <SyntaxHighlighter
                                      language="html"
                                      style={prism}
                                    >
                                      {payload_str}
                                    </SyntaxHighlighter>
                                  </Typography>
                                </td>
                                {/*  */}
                                <td className={className + " w-1/4"}>
                                  <Typography
                                    color="blue"
                                    className="whitespace-pre-wrap bg-gray-200 py-2 px-4 rounded-md"
                                  >
                                    <a
                                      href={matched_at}
                                      className="text-blue-500 hover:text-blue-700 text-sm underline font-mono"
                                      target="_blank"
                                    >
                                      {matched_at}
                                    </a>
                                  </Typography>
                                </td>
                                <td className={className}>
                                  <Button
                                    name={id}
                                    // href={`/vulnerabilities/vulnerabilitydetails/${id}`}
                                    onClick={navigateToVulnerabilityDetails}
                                    color="black"
                                  >
                                    details
                                  </Button>
                                </td>
                              </tr>
                            );
                          }
                        }
                      )}
                    </tbody>
                  </table>
                )) || (
                  <div className="mx-2 px-2">
                    <div className="mb-12 grid gap-12 py-8 grid-cols-1 place-items-center">
                      <img src={no_results} className="w-96 h-96" />
                    </div>
                  </div>
                )}
              </CardBody>
            </Card>
          </div>
        </CardBody>
      </Card>
    </>
  );
}
