import React, { useState } from "react";

import {
  Card,
  CardBody,
  Typography,
  Button,
  Input,
  Textarea,
  Select,
  Option,
  Alert,
} from "@material-tailwind/react";
import {
  PlayIcon,
  ChevronDoubleDownIcon,
  ChevronUpIcon,
  ChevronDoubleUpIcon,
  FolderArrowDownIcon,
} from "@heroicons/react/24/solid";

export default function BurpsuiteExport() {
  const [name, setName] = useState("");
  const [scope, setScope] = useState("");
  const [power, setPower] = useState(1);
  const [burpExport, setBurpExport] = useState();

  const [showAlerts, setShowAlerts] = useState(false);

  const handleFileChange = (e) => {
    if (e.target.files) {
      setBurpExport(e.target.files[0]);
    }
  };

  const reset = () => {
    setName("");
    setScope("");
    setPower(1);
    setBurpExport();
  };

  const handleSubmit = () => {
    if (!burpExport) {
      return;
    }
    let form_data = new FormData();
    form_data.append("name", name);
    form_data.append("scope", scope);
    form_data.append("power", power);
    form_data.append("burpExport", burpExport, burpExport.name);

    fetch("http://rune-api:8334/rune/v1/burpExport", {
      method: "POST",
      body: form_data,
    })
      .then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.error(err));

    reset();
    setShowAlerts(true);
  };

  return (
    <>
      <Alert
        key="green"
        open={showAlerts}
        color="green"
        className="mb-8"
        onClose={() => setShowAlerts(false)}
      >
        Successfully uploaded the burpsuite export
      </Alert>
      <div className="flex items-center gap-6">
        <div className="rounded-lg blue border border-blue-gray-900 w-20 h-20 justify-center items-center flex">
          <FolderArrowDownIcon fill="blue-gray" className="w-8 h-8" />
        </div>
        <div>
          <Typography variant="h6" color="blue-gray" className="mb-1 uppercase">
            Burpsuite Export
          </Typography>
          <Typography
            variant="small"
            className="font-normal text-blue-gray-600"
          >
            Export APIs from Burpsuite in xml format and import to Bolt
          </Typography>
        </div>
      </div>
      <div className="mb-12 grid gap-12 py-8 grid-cols-1 place-items-center">
        <Card className="w-full flex items-center">
          <CardBody className="max-w-[24rem]">
            <form className="flex flex-col gap-4">
              <div>
                <Typography
                  variant="small"
                  color="blue-gray"
                  className="mb-2 font-medium"
                >
                  Scan Name
                </Typography>
                <Input
                  type="text"
                  placeholder="FK_12/12/2023"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
                  labelProps={{
                    className: "before:content-none after:content-none",
                  }}
                />
              </div>

              <div className="my-3">
                <Typography
                  variant="small"
                  color="blue-gray"
                  className="mb-2 font-medium "
                >
                  Scope
                </Typography>

                <Textarea
                  placeholder="abc.com&#10;def.com"
                  value={scope}
                  onChange={(e) => setScope(e.target.value)}
                  className="!border-t-blue-gray-200 focus:!border-t-gray-900"
                  labelProps={{
                    className: "before:content-none after:content-none",
                  }}
                />
                <div className="my-4">
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="mb-2 font-medium"
                  >
                    Power
                  </Typography>
                  <Select
                    placeholder="Low"
                    value={power}
                    onChange={(e) => setPower(e)}
                    className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
                    labelProps={{
                      className: "before:content-none after:content-none",
                    }}
                    menuProps={{ className: "h-32" }}
                  >
                    <Option value={1}>
                      <div className="flex items-center gap-x-2">
                        <ChevronDoubleDownIcon className="h-4 w-4 rounded-full object-cover" />
                        Low
                      </div>
                    </Option>
                    <Option value={2}>
                      <div className="flex items-center gap-x-2">
                        <ChevronUpIcon className="h-4 w-4 rounded-full object-cover" />
                        Medium
                      </div>
                    </Option>
                    <Option value={3}>
                      <div className="flex items-center gap-x-2">
                        <ChevronDoubleUpIcon className="h-4 w-4 rounded-full object-cover" />
                        High
                      </div>
                    </Option>
                  </Select>
                </div>
                <Typography
                  variant="small"
                  color="blue-gray"
                  className="mb-2 font-medium"
                >
                  Burpsuite Export
                </Typography>
                <input
                  className="relative m-0 block w-full flex-auto rounded border border-solid border-black-900 bg-clip-padding px-3 py-[0.32rem] text-base font-normal text-neutral-700 transition duration-300 ease-in-out file:-mx-3 file:-my-[0.32rem] file:overflow-hidden file:rounded-none file:border-0 file:border-solid file:border-inherit file:bg-neutral-100 file:px-3 file:py-[0.32rem] file:text-neutral-700 file:transition file:duration-150 file:ease-in-out file:[border-inline-end-width:1px] file:[margin-inline-end:0.75rem] hover:file:bg-neutral-200 focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:file:bg-neutral-700 dark:file:text-neutral-100 dark:focus:border-primary"
                  type="file"
                  onChange={handleFileChange}
                  labelProps={{
                    className: "before:content-none after:content-none",
                  }}
                />
              </div>
              <Button size="lg" onClick={handleSubmit}>
                Scan Now
              </Button>
              <Typography
                variant="small"
                color="gray"
                className="mt-2 flex items-center justify-center gap-2 font-medium opacity-60"
              >
                <PlayIcon className="-mt-0.5 h-4 w-4" /> This will generate a
                plan for testing
              </Typography>
            </form>
          </CardBody>
        </Card>
      </div>
    </>
  );
}
