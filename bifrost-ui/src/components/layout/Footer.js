import React from 'react'
import { Typography } from "@material-tailwind/react";
import { HeartIcon } from "@heroicons/react/24/solid";

export default function Footer() {
    return (
        <>
            <footer className="py-2">
                <div className="flex w-full flex-wrap items-center justify-center gap-6 px-2 md:justify-between">
                    {/* <Typography variant="small" className="font-normal text-inherit">
                        &copy; 2023, made with{" "}
                        <HeartIcon className="-mt-0.5 inline-block h-3.5 w-3.5 text-red-600" /> by{" "}
                        <a
                            href="katsuro.shop"
                            target="_blank"
                            className="transition-colors hover:text-blue-500 font-bold"
                        >
                            katsuro
                        </a>{" "}
                        for a better web.
                    </Typography> */}
                    <ul className="flex items-center gap-4">
                        <li key="license">
                            <Typography
                                as="a"
                                href="/home"
                                target="_blank"
                                variant="small"
                                className="py-0.5 px-1 font-normal text-inherit transition-colors hover:text-blue-500"
                            >
                                license
                            </Typography>
                        </li>
                        <li key="aboutus">
                            <Typography
                                as="a"
                                href="/home"
                                target="_blank"
                                variant="small"
                                className="py-0.5 px-1 font-normal text-inherit transition-colors hover:text-blue-500"
                            >
                                about us
                            </Typography>
                        </li>
                        <li key="blog">
                            <Typography
                                as="a"
                                href="/home"
                                target="_blank"
                                variant="small"
                                className="py-0.5 px-1 font-normal text-inherit transition-colors hover:text-blue-500"
                            >
                                blog
                            </Typography>
                        </li>
                    </ul>
                </div>
            </footer>
        </>
    )
}
