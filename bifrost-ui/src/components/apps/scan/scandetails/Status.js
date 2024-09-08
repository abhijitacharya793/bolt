import React, { useEffect, useState } from "react";
import { useParams } from "react-router";
import {
  ArrowRightCircleIcon,
  ArrowRightIcon,
  CheckBadgeIcon,
} from "@heroicons/react/24/solid";
import { BoltIcon } from "@heroicons/react/24/outline";

import {
  Avatar,
  Button,
  Card,
  CardBody,
  CardHeader,
  IconButton,
  Typography,
} from "@material-tailwind/react";

export default function Status() {
  const params = useParams();

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
  const getResults = (scan_id) => {
    fetch(`http://hiemdall-api:8338/hiemdall/v1/result?scan_id=${scan_id}`, {
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
    getResults(params["id"]);
    getRisks();
    getTags();
  }, []);

  return (
    <div>
      <div className="flex">
        <div className=" bg-red-300 w-1/2 rounded-lg shadow-md border border-red-500 text-center items-center">
          <div className="my-10 mx-4">
            <p className="pt-10 pb-10 uppercase font-bold text-white">
              Threat Level
            </p>
            <p className="py-10 text-6xl flex items-center justify-center text-white">
              <BoltIcon className="w-14 h-14" /> Critical
            </p>
            <p className="mx-4 py-4 px-8 rounded-md bg-white whitespace-break-spaces">
              You should fix your critical severity issues immediately to avoid
              a breach.
            </p>
          </div>
        </div>
        <div className="w-2/3 pl-4">
          <div className="flex space-x-4 items-center rounded-md pr-4 bg-clip-border bg-gradient-to-tr from-gray-900 to-gray-800 text-white shadow-gray-900/20 shadow-lg">
            <div className="mx-4 my-2 w-2/3">
              <Typography
                variant="h5"
                color="white"
                className="text-base uppercase font-light"
              >
                Issues
              </Typography>
              <Typography variant="h1" color="white" className="font-light">
                {results.length}
              </Typography>
            </div>
            <a href="#" className="inline-block w-1/3">
              <Button
                size="sm"
                variant="text"
                className="flex items-center gap-2 text-white"
              >
                See all
                <ArrowRightIcon className="text-white w-4" />
              </Button>
            </a>
          </div>

          <div className="up flex items-center justify-center">
            <div className="bg-red-50 w-1/2 mt-4 mr-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">Critical</span>
              <span className="text-6xl">
                {
                  results.filter(function (res) {
                    return (
                      vulnerabilities[res.vulnerability_id - 1] && vulnerabilities[res.vulnerability_id - 1].severity === "c"
                    );
                  }).length
                }
              </span>
            </div>
            <div className="bg-orange-50 w-1/2 mt-4 ml-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">High</span>
              <span className="text-6xl">
                {
                  results.filter(function (res) {
                    return (
                      vulnerabilities[res.vulnerability_id - 1] && vulnerabilities[res.vulnerability_id - 1].severity === "h"
                    );
                  }).length
                }
              </span>
            </div>
          </div>
          <div className="down flex">
            <div className="bg-yellow-50 w-1/2 mt-4 mr-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">Medium</span>
              <span className="text-6xl">
                {
                  results.filter(function (res) {
                    return (
                      vulnerabilities[res.vulnerability_id - 1] && vulnerabilities[res.vulnerability_id - 1].severity === "m"
                    );
                  }).length
                }
              </span>
            </div>
            <div className="bg-green-50 w-1/2 mt-4 ml-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">Low</span>
              <span className="text-6xl">
                {
                  results.filter(function (res) {
                    return (
                      vulnerabilities[res.vulnerability_id - 1] && vulnerabilities[res.vulnerability_id - 1].severity === "l"
                    );
                  }).length
                }
              </span>
            </div>
          </div>
        </div>
      </div>
      <div className="bg-blue-50 rounded-lg shadow-md border border-blue-500 mt-4 p-4 flex items-center justify-start">
        <div className="pr-4">
          <CheckBadgeIcon className="w-10 h-10 text-green-500" />
        </div>
        <div className="">
          <p>Prominent issue</p>
          <p>There are no issues past their remediation date, good job!</p>
        </div>
      </div>
    </div>
  );
}
